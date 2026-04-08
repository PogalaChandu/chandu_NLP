import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.util import bigrams
from collections import defaultdict


text = "I love NLP and I love Python"
tokens = word_tokenize(text)

# Create bigram model
model = defaultdict(list)
for w1, w2 in bigrams(tokens):
    model[w1].append(w2)

# Generate text
word = "I"
generated = [word]

for i in range(5):
    next_word = random.choice(model[word])
    generated.append(next_word)
    word = next_word

print("Generated Text:", " ".join(generated))