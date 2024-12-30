import pandas as pd
from sklearn.model_selection import train_test_split
from src.data_processing import preprocess_data
from src.feature_engineering import vectorize_text
from src.models import train_logistic_regression, evaluate_model
from src.database import create_connection, create_table, insert_data, load_data_from_db
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "http://localhost:3000"}})

db_file = 'data/spam_detection.db'

def train_and_save_model():
    data_dir = 'data/raw/' 
    df = pd.concat([pd.read_csv(f"{data_dir}{file}") for file in ["Psy.csv", "KatyPerry.csv", "LMFAO.csv", "Eminem.csv", "Shakira.csv"]], ignore_index=True)
    df = preprocess_data(df)

    conn = create_connection(db_file)
    create_table(conn)
    insert_data(conn, df)
    df = load_data_from_db(conn)

    X, vectorizer = vectorize_text(df)
    y = df['CLASS']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = train_logistic_regression(X_train, y_train)

    metrics = evaluate_model(model, X_test, y_test)
    print(metrics)

    joblib.dump(model, 'model/spam_classifier.pkl')
    joblib.dump(vectorizer, 'model/vectorizer.pkl')
    return model, vectorizer

model, vectorizer = train_and_save_model()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  
    comment = data.get('comment', '')  
    if not comment:
        return jsonify({'error': 'No comment provided'}), 400

    vectorized_comment = vectorizer.transform([comment])
    prediction = model.predict(vectorized_comment)[0]
    result = 'spam' if prediction == 1 else 'not spam'

    return jsonify({'comment': comment, 'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)