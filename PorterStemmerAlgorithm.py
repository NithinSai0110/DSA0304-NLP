import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
porter_stemmer = PorterStemmer()
words = ["jumps", "jumping", "jumper", "jumped", "easily", "running", "flies", "flying", "flies"]
print("Before stemming:")
for word in words:
    print(word, end=", ")
print("\n\nAfter stemming:")
for word in words:
    stemmed_word = porter_stemmer.stem(word)
    print(stemmed_word, end=", ")