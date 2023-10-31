import spacy

nlp = spacy.load('en_core_web_sm')
sentence = "The cat on the roof, purring softly, which belongs to my neighbor, caught a mouse."
doc = nlp(sentence)

# Print token information
for token in doc:
    print(f"Token: {token.text}, Lemma: {token.lemma_}, Pos: {token.pos_}")

# Prepositional phrases
prepositional_phrases = [chunk.text for chunk in doc.noun_chunks if "on" in [token.text for token in chunk]]
print("In Prepositional Phrases:", prepositional_phrases)

# Gerundive phrases
gerundive_phrases = [chunk.text for chunk in doc.noun_chunks if "ing" in [token.text[-3:] for token in chunk]]
print("In Gerundive Phrases:", gerundive_phrases)

# Infinitive clauses
infinitive_clauses = [token.text for token in doc if token.dep_ == "xcomp"]
print("In Non-finite clauses (Infinitive Clauses):", infinitive_clauses)

# Relative clauses
relative_clauses = [token.text for token in doc if token.dep_ == "relcl"]
print("In Relative clauses:", relative_clauses)
