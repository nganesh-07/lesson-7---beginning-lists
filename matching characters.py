def matching(words):
    counter = 0
    list = []
    for word in words:
        if len(word) > 0 and word[0] == word[-1]:
            counter += 1
            list.append(word)
    print("A list of words with the same first and last character:", list)
    return counter

count = matching(["xyz", "afa", "afk", "cdc", "sos", "100", "505"])
print("The number of words that have the same first and last character are:", count)