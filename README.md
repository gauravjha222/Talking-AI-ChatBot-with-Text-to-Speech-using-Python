<h1> AI Voice Assistant </h1>

This project is a real-time conversational AI assistant that listens to your voice, understands what you say using AssemblyAI, generates intelligent responses using OpenAI GPT, and replies back to you with lifelike speech using ElevenLabs.



<h2> Features </h2> 

🎤 Real-time Speech Recognition — Converts your voice to text using AssemblyAI.

🧠 AI-Powered Responses — Uses OpenAI GPT to generate intelligent and contextual replies.

🔊 Text-to-Speech Output — Speaks responses aloud using ElevenLabs.

⚡ Continuous Conversation Loop — Keeps listening and responding in a natural conversation flow.


<h2> 🧩 Tech Stack </h2>

Python 3.8+

AssemblyAI SDK — for real-time transcription

OpenAI API — for chat completions

ElevenLabs API — for voice generation

Queue — to manage incoming transcripts




<h2>  How to run the Streamlit app </h2>

Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run main.py


Open the URL provided in the terminal, usually http://localhost:8501.

This setup gives you both a terminal-based AI assistant (app.py) and a web-based interactive version (main.py).
