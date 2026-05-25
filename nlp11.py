grammar = {
    "S": [["NP", "VP"]],
    "NP": [["dog"], ["cat"]],
    "VP": [["runs"], ["eats"]]
}

def parse(symbol, words):
    if not words:
        return False
    
    if symbol not in grammar:
        return words[0] == symbol and len(words) == 1

    for rule in grammar[symbol]:
        if len(rule) == len(words):
            if all(parse(r, [w]) for r, w in zip(rule, words)):
                return True
    return False

sentence = ["dog", "runs"]
print("Accepted" if parse("S", sentence) else "Rejected")