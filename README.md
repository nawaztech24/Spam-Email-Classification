# Spam-Email-Classification
This project is a simple machine learning based Spam Email Classification system.  
It classifies an email as *Spam* or *Ham (Not Spam)* using Natural Language Processing (NLP) techniques.
Email spam is a common problem today. Unwanted promotional and fraudulent emails waste time and can be harmful.  
The goal of this project is to build a basic spam detection system using Python and machine learning that can automatically identify spam emails.

## Technologies Used
- Python  
- Machine Learning  
- Natural Language Processing (NLP)  
- Scikit-learn  
- Pandas  
- NumPy  
- Jupyter Notebook
  
## Dataset
The dataset used in this project is `spam.csv`.  
It contains labeled email messages where:
- **spam** represents unwanted or promotional emails
- **ham** represents normal and safe email.
  
## Project Files
- `Spam_Email_Detector.py`  
  Python script used to load the trained model and predict whether an email is spam or ham.

- `Spam Email.ipynb`  
  Jupyter Notebook used for data preprocessing, model training, and evaluation.

- `spam.csv`  
  Dataset containing labeled email messages.

- `spam.pkl`  
  Trained machine learning model saved using pickle.

- `vectorizer.pkl`  
  Count/TF-IDF vectorizer used to convert text data into numerical format.

- `Screenshot of Ham Email.JPG`  
  Example output showing a non-spam email.

- `Screenshot of Spam Email.JPG`  
  Example output showing a spam email.
  
## How It Works
1. Email text is taken as input  
2. Text is cleaned and processed using NLP techniques  
3. The trained vectorizer converts text into numerical form  
4. The machine learning model predicts whether the email is spam or ham  
5. The result is displayed to the user
   
## How to Run the Project
How to Run the Project

1. Clone the repository
2. Make sure Python is installed on your system
3. Install required libraries:
   pip install pandas numpy scikit-learn streamlit
4. Run the application:
   python -m streamlit run Spam_Email_Detector.py



## Output
The system displays whether the given email is **Spam** or **Ham** based on the trained model.

## Future Improvements
- Improve accuracy using advanced NLP techniques  
- Add a graphical user interface (GUI)  
- Deploy the model as a web application  
- Train the model with a larger dataset

