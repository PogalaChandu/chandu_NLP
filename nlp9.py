import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

nltk.download('punkt')

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*s$', 'NNS'),
    (r'.*', 'NN')
]

tagger = RegexpTagger(patterns)

text = "Dogs are running and jumped"
words = word_tokenize(text)

print(tagger.tag(words))