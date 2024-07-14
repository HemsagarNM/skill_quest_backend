import os 
from dotenv import load_dotenv,dotenv_values
import json
import base64
LLM_API_KEY="AIzaSyAKa85QiN9DNDoAzOyTyGliOrRD1bNbtb8"
groq_api_key ="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"



firebaseConfig = {
  "apiKey": "AIzaSyB62MXfUgAR1HZxQaTtMo48cHZDxY4vbH4",
  "authDomain": "something-c3e3d.firebaseapp.com",
  "projectId": "something-c3e3d",
  "storageBucket": "something-c3e3d.appspot.com",
  "messagingSenderId": "460025255678",
  "appId": "1:460025255678:web:d23d0fef2c6630ea8037af",
  "measurementId": "G-HZXJ590PXW",
  'databaseURL': ""
}


load_dotenv()
def get_db_url():
    return DATABASE

def get_llm_api_key():
    return LLM_API_KEY

def get_groq_api_key():
    return groq_api_key

def get_service_account():
    return service_account


def get_firebase_config():
    return firebaseConfig



 




if __name__ == "__main__":
    print(get_llm_api_key())
    print(get_db_url())
    print(get_firebase_config())
    print(get_service_account())