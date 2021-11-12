import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text: str) -> str:
 # Translate from French to English
    """Translates from English to French"""
    if not english_text:
        return ''

    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()

    french_text = translation.get('translations')[0]['translation']

    return french_text

def french_to_english(french_text: str) -> str:
# Translate from English to French
    """Transaltes from French to English"""
    if not french_text:
        return ''

    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()

    english_text = translation.get('translations')[0]['translation']

    return english_text
