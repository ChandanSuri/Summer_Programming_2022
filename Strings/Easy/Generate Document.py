def generateDocument(characters, document):
    if len(document) == 0:
        return True

    charMap = dict()
    for char in characters:
        charMap[char] = charMap.get(char, 0) + 1

    for char in document:
        if char not in charMap or charMap[char] == 0:
            return False

        charMap[char] -= 1

    return True
