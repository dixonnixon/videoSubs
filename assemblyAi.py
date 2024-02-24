import requests
from bs4 import BeautifulSoup
import vimeo


import base64
from playwright.sync_api import sync_playwright
from pathlib import Path
import webvtt
from dotenv import load_dotenv

from moviepy.editor import *
import speech_recognition as sr
# https://www.assemblyai.com/blog/create-vtt-files-for-videos-python/

import os
import json
import assemblyai as aai

aai.settings.api_key = "API_KEY_ASSEMBLY"

load_dotenv()

transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)