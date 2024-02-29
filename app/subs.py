import requests
from bs4 import BeautifulSoup

import base64
# from playwright.sync_api import sync_playwright
from pathlib import Path
# import webvtt
from dotenv import load_dotenv

from moviepy.editor import *
import speech_recognition as sr

import os
import json

from ClientFactory import ClientFactory
from client_utils import get_client, create_vimeo_client

load_dotenv()

api_client_config = {
   "vimeo": {
        "token": os.environ.get("VIMEO_ACCESS"),
        "key": os.environ.get("VIMEO_CLIENT_ID"),
        "secret": os.environ.get("VIMEO_CLIENT_SECRET")
    }
}


# 915051800/baf3fdcde5') 

def with_client(client):
  print("with_client", client)
  def get_data(video_id, quality):
    response = client.get('https://player.vimeo.com/video/' + str(video_id) + '/config')

    files = response.json()['request']['files']['progressive']

    for file in files:
      if file['quality'] == quality:
        video_url = file['url']
        video_name = str(video_id) + '_' + file['quality'] + '.mp4'
        video_response = requests.get(video_url)

        video_file = open(video_name, 'wb')
        video_file.write(video_response.content)
        video_file.close()
        return video_name
      
  return get_data

def with_token(token: str):
    def get_data(video_id):
        headers = {
          "Authorization": f"Bearer {token}",
          "Accept": "application/vnd.vimeo.*+json;version=3.4"
        }
        print(headers, video_id)

        try:
          req = requests.get(f"https://api.vimeo.com/videos/{video_id}",
            headers = headers
          )
          res = req.json()
        except requests.exceptions.RequestException as e:
          print(e)
          print(res)
          return None
        
        print(req.status_code)
        # Use token to access data from url
        pass
    return get_data


def getToken(client_id, client_secret):
  authorization = base64.b64encode(bytes(client_id + ":" + client_secret, "ISO-8859-1")).decode("ascii")
  headers = {
    "Authorization": f"Basic {authorization}",
    "Content-Type": "application/json",
    "Accept": "application/vnd.vimeo.*+json;version=3.4"
  }

  body = {
    "grant_type": "client_credentials",
    "scope": "public"
  } 

  try:
    req = requests.post('https://api.vimeo.com/oauth/authorize/client',
      headers = headers,
      json=body
    )
  except requests.exceptions.RequestException as e:
    print(e)
    return None
  res = req.json()
  return res['access_token']




def mp4towav(mp4file, wavfile):
    videoclip=VideoFileClip(mp4file)
    audioclip=videoclip.audio
    audioclip.write_audiofile(wavfile,codec='pcm_s16le')
    audioclip.close()
    videoclip.close()

def audio_vtt_export(filename):
  r = sr.Recognizer()
  comments = sr.AudioFile(filename)
  with comments as source:
    audio = r.record(source)
    text = r.recognize_google(audio)
    print(text)





# save_track = with_token(getToken(
#   os.getenv('VIMEO_CLIENT_ID'),
#   os.getenv('VIMEO_CLIENT_SECRET')
# ))
    
client_factory = ClientFactory()
client_factory.register("vimeo", create_vimeo_client)

save_track = with_client(
  get_client('vimeo', client_factory, api_client_config)
)

mp4towav(save_track(355336541, '360p'), "audio.wav")
audio_vtt_export("audio.wav")


# response = client.get('https://player.vimeo.com/video/' + str(video_id) + '/config')

# files = response.json()['request']['files']['progressive']

# for file in files:
#   if file['quality'] == target_quality:
#     video_url = file['url']
#     video_name = str(video_id) + '_' + file['quality'] + '.mp4'
#     video_response = requests.get(video_url)

#     video_file = open(video_name, 'wb')
#     video_file.write(video_response.content)
#     video_file.close()

    # print('downloaded: ' + video_name)
#     mp4towav(video_name,"audio.wav")




# def getTextfromVideo():
#   #try load dynamic
#   target_link = None

#   with sync_playwright() as p:
#     browser = p.chromium.launch()
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto('https://vimeo.com/915051800/baf3fdcde5')
#     page.wait_for_load_state()
#     page.wait_for_timeout(8000)
#     page.wait_for_timeout(8000)
    
#     html = page.content()
#     bs = BeautifulSoup(html, 'html.parser')
#     track = bs.select("track")
#     target_link = "https://vimeo.com" + track[0]['src']
#     print(track[0]['src'])
    

#     # sometime later...
#     page.wait_for_timeout(8000)
#     # page.remove_listener("request", handle_request)
#     # page.remove_listener("request", load_tracker)
#     browser.close()

#   if target_link:
#     headers = {
#       "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) \
#           AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 \
#           Safari/9537.53"
#     }

#     print('requesting ', target_link)
#     try:
#       req = requests.get(target_link, headers=headers)
#     except requests.exceptions.RequestException as e:
#       print(e)

#     with open(str(Path.cwd()) + "/text.vtt", "w") as file1:
#       # Writing data to a file
#       file1.write(req.text)

#     out_text = ""
#     for caption in webvtt.read(str(Path.cwd()) + "/text.vtt"):
#       out_text += caption.text
#       print(caption.text)

#     with open(str(Path.cwd()) + "/text.txt", "w") as file2:
#       # Writing data to a file
#       file2.write(out_text)

