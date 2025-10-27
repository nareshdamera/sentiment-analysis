Sentiment Analysis Project Overview
This project implements a sentiment analysis system using machine learning to classify text as either Positive or Negative. Here's a breakdown of the key components:

Dataset
Used a large dataset of 1.6M text samples
Binary classification: 0 (Negative) and 1 (Positive)
Data was split 80-20 for training and testing
Text Preprocessing
Models Trained
Three different models were implemented and compared:

Logistic Regression
Support Vector Machine (LinearSVC)
Naive Bayes
Best Model Performance (Logistic Regression)

Precision: 0.78
Recall: 0.79
F1-score: 0.77
Accuracy: ~77%
Model Deployment
The best performing model (Logistic Regression) was saved using joblib
Implemented as a Streamlit web application for real-time sentiment prediction
Clean interface allowing users to input text and get immediate sentiment predictions
The project demonstrates strong performance in sentiment classification with balanced metrics, making it suitable for real-world applications.

Claude Sonnet 3.5 • 0.9x
