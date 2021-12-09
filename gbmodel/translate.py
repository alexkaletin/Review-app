# Imports the Google Cloud Translation library
from google.cloud import translate_v2 as translate
import six

def translate_text(text, language):
    #instanciates a client
    client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Translate text from english to specified language
    result = client.translate(text, target_language=language)

    return result["translatedText"]
    
