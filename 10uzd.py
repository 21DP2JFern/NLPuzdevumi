from googletrans import Translator

translator = Translator()
texts = ["Labdien! Kā jums klājas?", "Es šodien lasīju interesantu grāmatu."]
for text in texts:
    translation = translator.translate(text, src="lv", dest="en")
    print(f"Latviešu: {text} - Angļu: {translation.text}")