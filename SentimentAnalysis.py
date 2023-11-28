from textblob import TextBlob
sentences = [
    "I love this product! It's amazing.",
    "The weather is terrible today."
]
for sentence in sentences:
    blob = TextBlob(sentence)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    print(f'Sentence: "{sentence}"\nSentiment: {sentiment}\n')
