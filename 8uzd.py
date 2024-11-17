import spacy

nlp = spacy.load("en_core_web_sm")
text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

doc = nlp(text)
for ent in doc.ents:
    print(f"Vienība: {ent.text} - Tips: {ent.label_}")
