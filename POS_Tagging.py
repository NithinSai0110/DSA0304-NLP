import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
texts = ["The sun is shining brightly", "I love reading interesting books"]
for text in texts:
    words = word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    print("\nOriginal Text:", text)
    print("Part-of-Speech Tags:")
    for word, pos_tag in pos_tags:
        print(f"{word}: {pos_tag}")