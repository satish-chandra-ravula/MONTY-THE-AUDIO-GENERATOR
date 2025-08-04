# MONTY-THE-AUDIO-GENERATOR


Introduction
Monty The Audio Generator is a text-to-speech (TTS) application designed to convert written text into spoken audio. This project allows users to upload documents or manually input text and generate audio output using a male or female voice. Built using Python and Streamlit, this application provides a simple and efficient way to convert text into speech, making it useful for various applications, including accessibility, content creation, and learning assistance.

Project Description
Monty The Audio Generator allows users to:
•	Upload PDF, DOCX, or TXT files to extract text.
•	Manually enter text in a text area.
•	Select a preferred voice (Male or Female) for speech conversion.
•	Convert the extracted or manually entered text into speech.
•	Listen to and download the generated audio file.
The application is built using Streamlit for the user interface, pyttsx3 for text-to-speech conversion, and PyPDF2 & python-docx for document processing.


Features
•	File Upload Support: Users can upload PDF, DOCX, or TXT files.
•	Text Extraction: Automatically extracts text from uploaded documents.
•	Manual Text Input: Users can enter custom text manually.
•	Voice Selection: Choose between Male and Female voices for audio output.
•	Audio Generation: Converts text into an MP3 audio file and plays it within the application.
•	Simple and Interactive UI: Built with Streamlit for easy interaction.


Technologies Used
•	Python (Primary Language)
•	Streamlit (For Web Interface)
•	pyttsx3 (Text-to-Speech Engine)
•	PyPDF2 (PDF Text Extraction)
•	python-docx (DOCX Text Extraction)
•	Tempfile & OS (For Temporary File Handling)


How It Works
1.	User uploads a PDF, DOCX, or TXT file or manually inputs text.
2.	The application extracts the text from the file (if uploaded).
3.	The user selects a preferred voice (Male/Female).
4.	The user clicks the "Convert to Speech" button.
5.	The text is processed and converted into an MP3 file using pyttsx3.
6.	The generated audio is played within the application.

   
Installation & Usage
Prerequisites
•	Install Python (3.x recommended)
•	Install required libraries using the following command: 
•	pip install streamlit pyttsx3 PyPDF2 python-docx

Running the Application
1.	Save the project script as app.py.
2.	Run the application using: 
3.	streamlit run app.py
4.	Open the browser and interact with the UI to upload files and generate speech.
   
Future Enhancements
•	Multi-language Support: Add support for different languages.
•	Download Option: Allow users to download generated audio.
•	Real-Time Speech Customization: Control speed and pitch of speech.
•	Improved UI/UX: Enhance the user experience with better design elements.


Conclusion
Monty The Audio Generator is a simple yet powerful tool that enables users to convert text into speech efficiently. With support for document uploads, manual text entry, and voice selection, it provides a flexible solution for various use cases. Future updates will include additional features to enhance usability and performance.


