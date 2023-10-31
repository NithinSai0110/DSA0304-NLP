import nltk
from nltk import CFG, ChartParser
cfg = CFG.fromstring("""
    S -> NP VP
    NP -> N | Det N
    VP -> V NP
    Det -> 'The' | 'a'
    N -> 'dogs' | 'loyal'
    V -> 'are'
""")
parser = ChartParser(cfg)
sentence = "The dogs are loyal"
tokens = sentence.split()
for tree in parser.parse(tokens):
    tree.pretty_print()

grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'house'
    V -> 'chased' | 'saw'
""")
parser = ChartParser(grammar)
sen = "the cat chased dog"
tokens = sen.split()
for tree in parser.parse(tokens):
    tree.pretty_print()