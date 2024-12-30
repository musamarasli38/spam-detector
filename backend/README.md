# Spam Comment Detector

## Overview

This project is a Spam Comment Detector that uses machine learning to classify text comments as spam or not spam. It is built using Python, pandas and scikit-learn. This is not the best spam detector out there, but it was a good exercise for learning machine learning and AI techniques.

## Installation and Setup

Windows

```bash
python -m venv venv
source venv\Scripts\activate
pip install -r requirements.txt
```

## How to use

Train model with present datasets using "python main.py". This also evaluates the logistic regression model that was used.
Predict if a comment is spam or ham with "pythong predict.py". Input your desired comment and hit enter. The script will clean, train and predict if the comment is spam or not.
