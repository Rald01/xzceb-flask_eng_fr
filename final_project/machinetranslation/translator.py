import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='{2018-05-01}',
    authenticator=authenticator
)

language_translator.set_service_url('url')
apikey = os.environ['apikey']
url = os.environ['url']

def englishToFrench(englishText):
    translate = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    frenchText = json.dumps(translate['translations'][0]['translation'])
    print(frenchText)
    return frenchText

def frenchToEnglish(frenchText):
    translate = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    englishText = json.dumps(translate['translations'][0]['translation'])
    print(englishText)
    return englishText