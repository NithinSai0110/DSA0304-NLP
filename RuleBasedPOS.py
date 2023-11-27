import re
sentence = "The cat is quick. The dog is bright. Islamlare is running quickly."
patterns = [
    (r'\b(?:The|the)\b', 'DET'),
    (r'\b(?:cat|dog)\b', 'NOUN'),
    (r'\b(?:islamlare)\b', 'VERB'),
    (r'\b(?:quickly|brightly)\b', 'ADV'),
    (r'\b(?:[A-Za-z]+)\b', 'NOUN')
]
pos_tags = []
for word in re.findall(r'\b\w+\b', sentence):
    for pattern, tag in patterns:
        if re.fullmatch(pattern, word):
            pos_tags.append((word, tag))
            break
    else:
        pos_tags.append((word, 'UNKNOWN'))
print("Original Sentence:", sentence)
print("Part-of-Speech Tags:")
for word, pos_tag in pos_tags:
    print(f"{word}: {pos_tag}")
