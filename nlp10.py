sentence = ["The", "dog", "is", "running"]

# Initial tagging (default NN)
tags = [(word, "NN") for word in sentence]

# Transformation rules
def transform(tags):
    new_tags = []
    for word, tag in tags:
        if word.lower() in ["is", "am", "are"]:
            new_tags.append((word, "VB"))
        elif word.endswith("ing"):
            new_tags.append((word, "VBG"))
        else:
            new_tags.append((word, tag))
    return new_tags

final_tags = transform(tags)

print(final_tags)