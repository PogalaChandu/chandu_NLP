import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'dog'
VP -> 'runs'
""")

parser = ChartParser(grammar)
sentence = "dog runs".split()

for tree in parser.parse(sentence):
    print(tree)