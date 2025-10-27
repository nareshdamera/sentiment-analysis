🧠 Sentiment Analysis Project

This project implements a Sentiment Analysis System using Machine Learning to classify text as Positive or Negative.
It includes model training, evaluation, and deployment using a Streamlit web application for real-time predictions.

📂 Dataset

Total Samples: 1.6 million text entries

Task Type: Binary Classification

0 → Negative

1 → Positive

Data Split: 80% Training, 20% Testing

🧹 Text Preprocessing

Removed stopwords, special characters, and punctuation

Converted all text to lowercase

Tokenized text data

Used TF-IDF Vectorization to convert text into numerical features

🤖 Models Implemented

Three machine learning models were trained and compared:

Logistic Regression

Support Vector Machine (LinearSVC)

Naive Bayes

🏆 Best Model — Logistic Regression
Metric	Score
Precision	0.78
Recall	0.79
F1-Score	0.77
Accuracy	~77%

The Logistic Regression model achieved the best overall performance with well-balanced precision and recall.

🚀 Model Deployment

Saved the trained model using Joblib

Built a Streamlit web application for real-time sentiment prediction

Simple and clean UI that allows users to:

Enter custom text

Instantly view sentiment prediction results (Positive/Negative)

💡 Key Highlights

End-to-end machine learning pipeline from data preprocessing to deployment

Balanced model performance suitable for real-world applications

Easily extendable for multiclass sentiment or emotion detection tasks

🧩 Tech Stack

Language: Python

Libraries: scikit-learn, pandas, numpy, joblib, Streamlit

Model: Logistic Regression

Deployment: Streamlit Web App


🖥️ How to Run the Project
# Clone the repository
git clone https://github.com/yourusername/sentiment-analysis.git

# Navigate into the project directory
cd sentiment-analysis

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
