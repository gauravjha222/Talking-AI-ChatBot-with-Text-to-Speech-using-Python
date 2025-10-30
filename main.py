
import streamlit as st
import openai
import elevenlabs

# Set API keys
openai.api_key = "YOUR_OPENAI_API_KEY"
elevenlabs.set_api_key("YOUR_ELEVENLABS_API_KEY")

st.title("AI Voice Assistant")

# Text input for user query
user_input = st.text_input("Ask me anything:")

if user_input:
    # Generate response using OpenAI GPT
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {"role": "system", "content": "You are a highly skilled AI, answer concisely."},
            {"role": "user", "content": user_input}
        ]
    )
    text = response['choices'][0]['message']['content']
    
    st.write("**AI:**", text)

    # Generate audio using ElevenLabs
    audio = elevenlabs.generate(text=text, voice="Bella")
    
    # Streamlit audio player
    st.audio(audio, format="audio/wav")
