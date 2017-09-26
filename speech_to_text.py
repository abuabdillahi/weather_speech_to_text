import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build

from weather import get_weather
from send_text import success_text, fail_text
from cities import get_cities

key="#######"

credentials = GoogleCredentials.get_application_default()

service = build('compute', 'v1', credentials=credentials)

import record_audio

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    'output.wav')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code='en-UK')

# Detects speech in the audio file
response = client.recognize(config, audio)
alternatives = response.results[0].alternatives

for alternative in alternatives:
    print('Transcript: {}'.format(alternative.transcript))
    cities = get_cities()
    for city in cities:
        if city in alternative.transcript:
            weather = get_weather(city)
            success_text(weather)
            break
    else:
        fail_text()
        

        