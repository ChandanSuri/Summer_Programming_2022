def isPalindrome(string):
    lenStr = len(string)
    if lenStr == 1 or lenStr == 0:
        return True

    leftIdx = 0
    rightIdx = lenStr - 1

    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1

    return True
