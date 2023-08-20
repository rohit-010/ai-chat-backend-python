import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")

# Elevent labs
# Convert Text to speech
def convert_text_to_speech(message):
  # Define body
  body={
    "text": message,
    "voice_settings": {
      "stability": 0,
      "similarity_boost":0,

    }
  }
  # Define voice
  voice_rachel = "21m00Tcm4TlvDq8ikWAM"
    
  headers={
    "xi-api-key": ELEVEN_LABS_API_KEY,
    "Content-Type": "application/json",
    "accept": "audio/mpeg"
  }
  # Endpoint
  endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}"

   
  # API_URL = "https://api-inference.huggingface.co/models/facebook/fastspeech2-en-ljspeech"
  # apitoken = config("HF_ACCESS_TOKEN")
  # huggingHeaders = {"Authorization": f"Bearer {apitoken}"}
   
  # Send request 
  try:
    response = requests.post(endpoint, json=body, headers=headers)
    # response = requests.post(API_URL, json=body, headers=huggingHeaders)
  except Exception as e:
    return

  #  handle response
  if response.status_code == 200:
    return response.content
  else:
    return 