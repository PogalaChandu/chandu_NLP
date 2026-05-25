import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'dog' [0.5] | 'cat' [0.5]
VP -> 'runs' [0.6] | 'eats' [0.4]
""")

parser = ViterbiParser(grammar)
sentence = "dog runs".split()

for tree in parser.parse(sentence):
    print(tree)