import re
sentence = "The quick brown fox jumps over the lazy dog"
rules = [
    (r'\b(?:The|the|A|a|An|an)\b', 'DT'),
    (r'\b(?:quick|brown|lazy)\b', 'JJ'),
    (r'\b(?:fox|dog)\b', 'NN'),
    (r'\b(?:jumps)\b', 'VB'),
    (r'\b(?:over)\b', 'IN'),
]
pos_tags = []
for word in sentence.split():
    for pattern, tag in rules:
        if re.fullmatch(pattern, word):
            pos_tags.append((word, tag))
            break
    else:
        pos_tags.append((word, 'UNKNOWN'))
print("Original Sentence:", sentence)
print("Part-of-Speech Tags:")
for word, pos_tag in pos_tags:
    print(f"{word}: {pos_tag}")
