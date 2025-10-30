import assemblyai as aai
import openai
import elevenlabs
from queue import Queue

# Set API keys
aai.settings.api_key = "e33712675652436cbdce680faa2781a4"
openai.api_key = "OPENAI_API_KEY"
elevenlabs.set_api_key("sk_632447d65c1d0b7e6b481c4569c7d48d89e34e24b379930b") 

transcript_queue = Queue()

def on_data(transcript: aai.RealtimeTranscript):
    if not transcript.text:
        return
    if isinstance(transcript, aai.RealtimeFinalTranscript):
        transcript_queue.put(transcript.text + '')
        print("User:", transcript.text, end="\r\n")
    else:
        print(transcript.text, end="\r")

def on_error(error: aai.RealtimeError):
    print("An error occured:", error)

# Conversation loop
def handle_conversation():
    while True:
        transcriber = aai.RealtimeTranscriber(
            on_data=on_data,
            on_error=on_error,
            sample_rate=44_100,
        )

        # Start the connection
        transcriber.connect()

        # Open  the microphone stream
        microphone_stream = aai.extras.MicrophoneStream()

        # Stream audio from the microphone
        transcriber.stream(microphone_stream)

        # Close current transcription session with Crtl + C
        transcriber.close()

        # Retrieve data from queue
        transcript_result = transcript_queue.get()

        # Send the transcript to OpenAI for response generation
        response = openai.ChatCompletion.create(
            model = 'gpt-4',
            messages = [
                {"role": "system", "content": 'You are a highly skilled AI, answer the questions given within a maximum of 1000 characters.'},
                {"role": "user", "content": transcript_result}
            ]
        )

        #text = response['choices'][0]['message']['content']
        text = "AssemblyAI is the best YouTube channel for the latest AI tutorials."

        # Convert the response to audio and play it
        audio = elevenlabs.generate(
            text=text,
            voice="Bella" # or any voice of your choice
        )

        print("\nAI:", text, end="\r\n")

        elevenlabs.play(audio)

handle_conversation()




