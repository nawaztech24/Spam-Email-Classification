import pickle
import streamlit as st
import pyttsx3
from datetime import datetime  # Importing datetime module

# Initialize pyttsx3 for text-to-speech
def speak(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, "voice.mp3")
    engine.runAndWait()
    st.audio("voice.mp3")

# Load model and vectorizer
model = pickle.load(open("spam.pkl", "rb"))
cv = pickle.load(open("vectorizer.pkl", "rb"))

# Function to predict the message
def predict_message(msg):
    data = [msg]
    vect = cv.transform(data).toarray()
    prediction = model.predict(vect)
    result = prediction[0]
    
    # Return prediction result
    return "Spam" if result == 1 else "Ham"

# Function to add history
def add_to_history(msg, result):
    if 'history' not in st.session_state:
        st.session_state.history = []  # Initialize the history list in session state if not already done
    st.session_state.history.append({'message': msg, 'prediction': result, 'timestamp': datetime.now()})

# Function to display history
def display_history():
    if 'history' in st.session_state and st.session_state.history:
        st.subheader("History")
        for idx, item in enumerate(st.session_state.history):
            timestamp = item['timestamp'].strftime('%Y-%m-%d %H:%M:%S')  # Format timestamp
            st.write(f"{idx + 1}. {item['message']} - {item['prediction']} - {timestamp}")

def main():
    # Display the title and description
    st.title("Email Spam Detector")
    st.subheader("Built by Mohd Nawaz Khan")

    # Input box for the user to enter a text
    msg = st.text_input("Enter a Text:", key="input_message")  # Use a unique key

    # Display prediction button
    if st.button("Predict"):
        # Perform prediction
        result = predict_message(msg)
        
        # Show the result and speak it
        if result == "Spam":
            # Use HTML and CSS to make the text bold and blinking
            spam_text = "<p style='font-size:24px; font-weight:bold; color:red; animation: blink 1s infinite;'>This is a <span style='font-weight:bold;'>Spam</span> mail</p>"
            st.markdown(spam_text, unsafe_allow_html=True)
            speak("This is a spam email")
        else:
            st.success("This is a ham email")
            speak("This is a Ham email")

        # Add the prediction result and message to history
        add_to_history(msg, result)

        # Horizontal line
        st.markdown("---")  # Horizontal line
        
        # Display the history below the line
        display_history()

# Add CSS for blinking effect
st.markdown("""
    <style>
        @keyframes blink {
            50% { opacity: 0; }
        }
    </style>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
