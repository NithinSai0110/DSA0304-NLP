from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
documents = [
    ("This is a positive document", "positive"),
    ("Negative sentiment here", "negative"),
    ("Spam email! Buy now!", "spam"),
    ("Great product, highly recommend", "positive"),
    ("Important meeting tomorrow", "neutral"),
    ("Claim your prize today", "spam"),
]
X, y = zip(*documents)
vectorizer = CountVectorizer()
X_vectors = vectorizer.fit_transform(X)
clf = MultinomialNB()
clf.fit(X_vectors, y)
new_examples = []
while True:
    user_input = input("Enter your messages (or type 'exit' to stop): ")
    if user_input.lower() == 'exit':
        break
    new_examples.append(user_input)
new_examples_vectors = vectorizer.transform(new_examples)
new_predictions = clf.predict(new_examples_vectors)
print("\nPredictions for new examples:")
for example, prediction in zip(new_examples, new_predictions):
    print(f"{example}: {prediction}")
