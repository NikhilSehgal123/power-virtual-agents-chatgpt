import openai
import requests
import json
import os
import pytube
import requests

openai.api_key = "YOUR API KEY"

system_content = """
You are a friendly agent called Neo.
"""

def generate_chatgpt_response(query):
    chatgpt = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": system_content},
            {"role": "user", "content": query}
            ]
        )
    return chatgpt["choices"][0]["message"]["content"]


def transcribe_youtube_video(url, api_key="YOUR API KEY", model="whisper-1"):
    # Download the audio from the YouTube video using pytube
    youtube = pytube.YouTube(url)
    audio = youtube.streams.filter(only_audio=True).first()
    audio_path = audio.download(output_path=".", filename_prefix="temp_")

    # Transcribe the audio using the OpenAI transcription API
    openai_url = "https://api.openai.com/v1/audio/transcriptions"
    openai_headers = {"Authorization": f"Bearer {api_key}"}
    openai_data = {"model": model}
    openai_files = {"file": (os.path.basename(audio_path), open(audio_path, "rb"))}
    openai_response = requests.post(openai_url, headers=openai_headers, data=openai_data, files=openai_files)
    transcription = openai_response.json()["text"]

    # Clean up temporary files
    os.remove(audio_path)

    # Return the transcription as a string
    return transcription

# Function for transcribing a youtube video and using ChatGPT to summarise it
def summarise_youtube_video(url, api_key="YOUR API KEY", model="whisper-1"):
    text_response = transcribe_youtube_video(url, api_key, model)
    chatgpt_prompt = """Can you help me to summarise this video? The transcript is below:\n{transcript}""".format(transcript=text_response)
    chatgpt_response = generate_chatgpt_response(chatgpt_prompt)
    return chatgpt_response

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=ABwDOd7K5is"
    summary = summarise_youtube_video(youtube_url)
    print(summary)

