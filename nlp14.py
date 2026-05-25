import nltk
from nltk import CFG
from nltk.parse import ChartParser
grammar = CFG.fromstring("""
S -> NP VP
NP -> 'he' | 'they'
VP -> 'runs' | 'run'
""")
parser = ChartParser(grammar)
sentence = "he runs".split()
try:
    trees = list(parser.parse(sentence))
    print("Correct" if trees else "Incorrect")
except:
    print("Incorrect")