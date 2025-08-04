import streamlit as st
import pyttsx3
import tempfile
import os
from PyPDF2 import PdfReader
import docx

def text_to_speech(text, voice_gender):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    # Set voice based on user selection
    if voice_gender == "Male":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_path = temp_file.name
    temp_file.close()
    engine.save_to_file(text, temp_path)
    engine.runAndWait()
    return temp_path

def extract_text_from_file(uploaded_file):
    text = ""
    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    elif uploaded_file.type == "text/plain":
        text = uploaded_file.read().decode("utf-8")
    return text

st.title("Monty The Speech Converter")

uploaded_file = st.file_uploader("Upload a PDF, DOCX, or TXT file", type=["pdf", "docx", "txt"])
user_input = st.text_area("Or enter text manually:")

# Select voice gender
voice_gender = st.selectbox("Select Voice", ["Male", "Female"])

text = ""
if uploaded_file is not None:
    text = extract_text_from_file(uploaded_file)
    st.text_area("Extracted Text", text, height=200)

if user_input.strip():
    text = user_input

if st.button("Convert to Speech"):
    if text.strip():
        audio_path = text_to_speech(text, voice_gender)
        st.audio(audio_path, format='audio/mp3')
        os.remove(audio_path)
    else:
        st.warning("No text found to convert.")

st.markdown("---")
st.markdown("© 2025 Monty The Audio Generator. All rights reserved to Sateesh.", unsafe_allow_html=True)
