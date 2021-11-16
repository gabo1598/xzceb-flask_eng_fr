"""
this on ingles, no entendechon
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv  import load_dotenv

load_dotenv()

apikey = os.environ['apikey']

"""esta funcion es lo maximo"""
url = os.environ['url']

"""esta funcion es lo maximo"""
authenticator = IAMAuthenticator(apikey)

"""esta funcion es lo maximo"""
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)

"""esta funcion es lo maximo"""
language_translator.set_service_url(url)


def english_to_french(english_text):
    """esta funcion es lo maximo"""
    translation_response = language_translator.translate(text=english_text, model_id='en-fr')
    translation=translation_response.get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """esta funcion es lo maximo"""
    translation_response = language_translator.translate(text=french_text, model_id='fr-en')
    translation=translation_response.get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
