import openai
from decouple import config
from functions.database import get_recent_messages
import json
import os
import requests
from huggingface_hub import InferenceClient
from bardapi import Bard


bardtoken = os.getenv("BARD_API_KEY")
bardapitoken = config("BARD_API_KEY")
 
print(bardapitoken) 
bard = Bard(token=bardapitoken)
apitoken = config("HF_ACCESS_TOKEN")
client = InferenceClient(token="{apitoken}")

headers = {"Authorization": f"Bearer {apitoken}"}

API_URL = "https://api-inference.huggingface.co/models/microsoft/speecht5_asr"

CHAT_API_URL = "https://api-inference.huggingface.co/models/microsoft/speecht5_asr"

# Retrieve Env Vars
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

# Open Ai - Whiseper 
# Convert Audio to Text
def convert_audio_to_text(audio_file):
    try:
      # transcript = openai.Audio.transcribe("whisper-1",audio_file)
      response = requests.request("POST", API_URL, headers=headers, data=audio_file)
      return json.loads(response.content.decode("utf-8"))["text"]
      # message_text = transcript["text"]
      # return message_text
    except Exception as e:
      print(e)
      return

# Chat model API
# Get Response of our message
def get_chat_response(message_input):
  
  messages=get_recent_messages()
  user_message={"role":"user","content":message_input}
  messages.append(user_message)
  print(messages[0])

  try:
    # response = "test"
    # response = bard.get_answer(messages)
    response = bard.get_answer(messages[0]["content"])
    print(response)
    message_text=response["choices"][1]
    return message_text
  except Exception as e:
    print(e)
    return 
