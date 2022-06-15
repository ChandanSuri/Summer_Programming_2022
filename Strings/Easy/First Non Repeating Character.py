# O(N) time and O(N) space
def firstNonRepeatingCharacter(string):
    charMap = dict()

    for char in string:
        charMap[char] = charMap.get(char, 0) + 1

    for idx, char in enumerate(string):
        if charMap[char] == 1:
            return idx

    return -1
