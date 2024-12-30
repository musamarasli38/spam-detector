import os
import joblib
import pandas as pd
from src.data_processing import preprocess_data

def load_model_and_vectorizer():
    #model_file = joblib.load('model/spam_classifier.pkl')
    #vectorizer_file = joblib.load('model/vectorizer.pkl')

    model_file = 'model/spam_classifier.pkl'
    vectorizer_file = 'model/vectorizer.pkl'

    # debug huidige folder
    print("Current directory:", os.getcwd())

    # model en vectorizer laden
    model = joblib.load(model_file)
    vectorizer = joblib.load(vectorizer_file)
    
    return model, vectorizer

def predict_comment(comment):
    model, vectorizer = load_model_and_vectorizer()

    # nieuwe dataframe voor input comment
    data = {'CONTENT': [comment]}
    df = pd.DataFrame(data)

    # clean nieuwe comment
    df = preprocess_data(df)

    # vector conversie  van ingegeven comment
    X = vectorizer.transform(df['CONTENT'])

    # Make a prediction
    prediction = model.predict(X)
    return prediction[0]

#invoer en uitvoer van comment en resultaat
if __name__ == "__main__":
    comment = input("Enter a comment: ")
    try:
        result = predict_comment(comment)
        if result == 1:
            print("This comment is spam.")
        else:
            print("This comment is not spam.")
    except Exception as e:
        print("Error during prediction:", e)
