from nltk.stem import PorterStemmer

words = ["running", "jumps", "easily", "flying"]

stemmer = PorterStemmer()

for word in words:
    print(word, "->", stemmer.stem(word))