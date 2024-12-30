# Explanation of Code Files and Techniques Used

## data_processing.py

This module handles data preprocessing tasks such as cleaning text, removing stopwords, and tokenizing text. It uses libraries like pandas for data manipulation.

## database.py

This module handles database interactions, including reading from and writing to the SQLite database (spam_detection.db). It uses the sqlite3 library for database operations.

## feature_engineering.py

This module extracts features from the text data. It includes functions to create TF-IDF vectors and other features used in the machine learning model.

## models.py

This module defines and trains the machine learning models. It includes functions to train a logistic regression model and save it as a pickle file.

## utils.py

This module contains utility functions that are used across different parts of the project. It includes functions for loading and saving models, handling file paths, etc.

## main.py

This script trains the machine learning model using the preprocessed and feature-engineered data. It saves the trained model and vectorizer as pickle files.

## predict.py

This script loads the trained model and vectorizer, and uses them to predict whether a given comment is spam or not. It prompts the user to enter a comment and outputs the prediction.

## Techniques and Libraries Used

    Pandas: Used for data manipulation and analysis.
    Scikit-learn: Used for machine learning tasks, including training and evaluating models.
    Joblib: Used for saving and loading machine learning models.
    SQLite3: Used for database operations.
