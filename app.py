import streamlit as st
import joblib
import re

# Load model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Text cleaning function (same as used in training)
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return text

# Streamlit UI
st.set_page_config(page_title="Sentiment Analysis App", page_icon="💬", layout="centered")

st.title("💬 Sentiment Analysis App")
st.write("Enter a text below and find out whether it's **Positive 😀** or **Negative 😞**")

# Input box
user_input = st.text_area("Enter your text here:")

if st.button("Analyze Sentiment"):
    if user_input.strip() != "":
        # Clean and transform
        clean = clean_text(user_input)
        vec = vectorizer.transform([clean])
        
        # Predict
        prediction = model.predict(vec)[0]
        
        if prediction == 1:
            st.success("Sentiment: Positive 😀")
        else:
            st.error("Sentiment: Negative 😞")
    else:
        st.warning("⚠️ Please enter some text!")
