
word_tag_prob = {
    "dog": {"NN": 0.9},
    "runs": {"VB": 0.8},
    "fast": {"RB": 0.7}
}

sentence = ["dog", "runs", "fast"]

tagged = []

for word in sentence:
    if word in word_tag_prob:
        tag = max(word_tag_prob[word], key=word_tag_prob[word].get)
    else:
        tag = "NN"
    tagged.append((word, tag))

print(tagged)