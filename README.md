

# Spam Email Classification System

This project is a Machine Learning-based Spam Email Classification system developed during the AICTE Internship – AI: Transformative Learning with TechSaksham (a joint CSR initiative of Microsoft & SAP, implemented by Edunet Foundation).

The system classifies email messages as:

- Spam (Unwanted / Fraudulent)  
- Ham (Legitimate Email)  

---

## Live Demo

https://your-app-link.streamlit.app

---


## Problem Statement

Email spam is a major issue that affects productivity and cybersecurity.  
The goal of this project is to build a spam detection system using NLP and Machine Learning techniques to automatically classify emails.

---

## Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  
- Pickle  

### Machine Learning Components

- CountVectorizer (Text Feature Extraction)  
- Multinomial Naive Bayes Classifier  

---

## Features

- Real-time spam detection  
- Confidence score for predictions  
- Dark-themed user interface  
- Text-to-speech feedback  
- Session-based history tracking  

---

## Project Structure

Spam_Email_Detector.py  
Spam Email.ipynb  
train_model.py  
spam.csv  
spam.pkl  
vectorizer.pkl  
style.css  
background.jpg  

---

## How It Works

1. User enters email text  
2. Text is converted into numerical vectors using CountVectorizer  
3. The trained Naive Bayes model predicts the class  
4. The result is displayed as Spam or Ham  
5. Prediction history is maintained during the session  

---

## How to Run

Install required libraries:

pip install pandas numpy scikit-learn streamlit gtts

Run the application:

streamlit run Spam_Email_Detector.py

---

## Model Information

- Algorithm: Multinomial Naive Bayes  
- Text Vectorization: CountVectorizer  
- Accuracy: (Add your result from notebook here)  

---

## Future Improvements

- Improve model accuracy  
- Use TF-IDF vectorization  
- Try advanced models (Logistic Regression / Deep Learning)  
- Deploy as a scalable web application  

---

## Author

Mohd Nawaz Khan


