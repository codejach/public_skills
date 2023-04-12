import os

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def gtts_speech(text):
    file_path = 'speech.mp3'

    tts = gTTS(text)
    tts.save(file_path)

    song = AudioSegment.from_mp3(file_path)
    play(song)

    os.remove(file_path)

def say(text):
    gtts_speech(text)
