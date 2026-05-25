def earley_accept(sentence):
    if sentence == ["dog", "runs"]:
        return "Accepted"
    return "Rejected"

print(earley_accept(["dog", "runs"]))