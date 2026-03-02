Spam Email Classification System

This project is a Machine Learning based Spam Email Classification system developed during the AICTE Internship – AI: Transformative Learning with TechSaksham (a joint CSR initiative of Microsoft & SAP, implemented by Edunet Foundation).

The system classifies email messages as:

Spam (Unwanted / Fraudulent)

Ham (Legitimate Email)

🎓 Internship Details

Developed as part of:

AI: Transformative Learning with TechSaksham
AICTE Internship Program
Joint CSR Initiative of Microsoft & SAP
Implemented by Edunet Foundation

This project demonstrates practical application of Machine Learning and NLP concepts.

📌 Problem Statement

Email spam is a major issue that affects productivity and cybersecurity.
The goal of this project is to build a basic spam detection model using Natural Language Processing and Machine Learning techniques to automatically classify emails.

🛠️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

Streamlit

Pickle

Machine Learning Components

CountVectorizer (Text Feature Extraction)

Multinomial Naive Bayes Classifier

📂 Project Structure
Spam_Email_Detector.py   → Streamlit web application
Spam Email.ipynb         → Model training & evaluation
train_model.py           → Model retraining script
spam.csv                 → Dataset
spam.pkl                 → Trained model
vectorizer.pkl           → Saved vectorizer
⚙️ How It Works

User enters email text.

Text is converted into numerical vectors using CountVectorizer.

The trained Naive Bayes model predicts the class.

The result is displayed as Spam or Ham.

Prediction history is maintained during the session.

▶️ How to Run

Install required libraries:

pip install pandas numpy scikit-learn streamlit pyttsx3

Run the application:

streamlit run Spam_Email_Detector.py
📊 Model Information

Algorithm: Multinomial Naive Bayes

Text Vectorization: CountVectorizer

Accuracy: (Add your result from notebook here)

🔮 Future Improvements

Improve model accuracy

Use TF-IDF vectorization

Try advanced models (Logistic Regression / Deep Learning)

Deploy as web application

