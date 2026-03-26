import pickle
import streamlit as st
from datetime import datetime
from gtts import gTTS
import base64

st.set_page_config(page_title="Spam Email Detector", page_icon="📧", layout="centered")

def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

bg_img = get_base64_image("background.jpg")

def speak(text):
    tts = gTTS(text)
    tts.save("voice.mp3")
    with open("voice.mp3", "rb") as f:
        audio_bytes = f.read()
    b64 = base64.b64encode(audio_bytes).decode()
    st.markdown(f"""
    <audio autoplay>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """, unsafe_allow_html=True)

model = pickle.load(open("spam.pkl", "rb"))
cv = pickle.load(open("vectorizer.pkl", "rb"))

def predict_message(msg):
    vect = cv.transform([msg]).toarray()
    prediction = model.predict(vect)[0]
    try:
        prob = model.predict_proba(vect)[0]
        confidence = max(prob) * 100
    except:
        confidence = 90
    return ("Spam" if prediction == 1 else "Ham"), round(confidence, 2)

def add_to_history(msg, result):
    if 'history' not in st.session_state:
        st.session_state.history = []
    st.session_state.history.append({
        'message': msg,
        'prediction': result,
        'timestamp': datetime.now()
    })

def display_history():
    if 'history' in st.session_state:
        st.markdown("### History")
        for item in reversed(st.session_state.history):
            time = item['timestamp'].strftime('%d %b %Y, %I:%M %p')
            st.markdown(f"""
            <div class="history-box">
                <b>Message:</b> {item['message']} <br>
                <b>Result:</b> {item['prediction']} <br>
                <small>{time}</small>
            </div>
            """, unsafe_allow_html=True)

st.markdown("<h1>Spam Email Detector</h1>", unsafe_allow_html=True)
st.markdown("<h3>Built by Mohd Nawaz Khan</h3>", unsafe_allow_html=True)

msg = st.text_input("Enter your message")

if st.button("Predict"):
    with st.spinner("Analyzing..."):
        result, confidence = predict_message(msg)

    if result == "Spam":
        st.markdown(f"<div class='result spam'>Spam Email Detected<br><small>Confidence: {confidence}%</small></div>", unsafe_allow_html=True)
        speak("This is a spam email")
    else:
        st.markdown(f"<div class='result ham'>Safe Email<br><small>Confidence: {confidence}%</small></div>", unsafe_allow_html=True)
        speak("This is a safe email")

    add_to_history(msg, result)
    display_history()

st.markdown(f"""
<style>

[data-testid="stAppViewContainer"] {{
    background: url("data:image/jpg;base64,{bg_img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.6);
    z-index: 0;
}}

.block-container {{
    background: rgba(0,0,0,0.75);
    backdrop-filter: blur(12px);
    color: white;
    padding: 40px;
    border-radius: 20px;
    max-width: 700px;
    margin: auto;
    margin-top: 60px;
    position: relative;
    z-index: 1;
}}

h1, h3, label {{
    color: white !important;
}}

input {{
    background-color: #2a2a2a !important;
    color: white !important;
    caret-color: white !important;
}}

input:focus {{
    outline: none !important;
    border: 1px solid #ff4b2b !important;
    box-shadow: 0 0 8px #ff4b2b;
}}

div.stButton > button {{
    background: #ff4b2b;
    color: white;
    border-radius: 10px;
    font-weight: bold;
}}

.result {{
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
}}

.spam {{
    background: #3a1a1a;
    color: #ff4b4b;
}}

.ham {{
    background: #1a3a1f;
    color: #4bff88;
}}

.history-box {{
    background: #2a2a2a;
    padding: 10px;
    border-radius: 8px;
    margin-top: 10px;
}}

</style>
""", unsafe_allow_html=True)