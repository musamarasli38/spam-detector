from sklearn.feature_extraction.text import TfidfVectorizer


#TFIDF vectors aanmaken van text gegevens, hiermee is de data klaar voor de model
def vectorize_text(data):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    X = vectorizer.fit_transform(data['CONTENT'])
    return X, vectorizer
