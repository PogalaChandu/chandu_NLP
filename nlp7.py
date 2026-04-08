import nltk

# Download required resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "Natural language processing is amazing"

tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)

print(tags)