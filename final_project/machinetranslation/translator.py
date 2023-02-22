import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
version = '2023-02-01'


def englishtofrench(englishtext):

    if englishtext is None:
        return None
    else:
        authenticator = IAMAuthenticator(apikey)
        translator = LanguageTranslatorV3(
            version=version, authenticator=authenticator)
        translator.set_service_url(url)
        l_t = translator
        translation = l_t.translate(
            text=englishtext, model_id="en-fr").get_result()
        return translation['translations'][0]['translation']


def frenchtoenglish(frenchtext):

    if frenchtext is None:
        return None
    else:
        authenticator = IAMAuthenticator(apikey)
        translator = LanguageTranslatorV3(
            version=version, authenticator=authenticator)
        translator.set_service_url(url)
        l_t = translator
        translation = l_t.translate(
            text=frenchtext, model_id="fr-en").get_result()
        return translation['translations'][0]['translation']
