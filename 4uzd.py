from deep_translator import GoogleTranslator
from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis")


def translate_and_analyze_sentiment(text, source_language='auto', target_language='en'):

    translated_text = GoogleTranslator(source=source_language, target=target_language).translate(text)
    print(f"Translated Text: {translated_text}")

    result = sentiment_analysis(translated_text)

    return result

texts = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",  
    "Esmu vīlies, produkts neatbilst aprakstam.",       
    "Neitrāls produkts, nekas īpašs."                    
]

for text in texts:
    sentiment = translate_and_analyze_sentiment(text)
    print(f"Original Text: {text}")
    print(f"Sentiment: {sentiment}\n")