import spacy
nlp = spacy.load("en_core_web_sm")
sentence = "Barack Obama was the 44th President of the United States, and he was born in Honolulu, Hawaii."
doc = nlp(sentence)
named_entities = [(ent.text, ent.label_) for ent in doc.ents]
print("Named Entities:")
for entity, label in named_entities:
    print(f"{entity} - {label}")
