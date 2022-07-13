class Solution(object):
    def __init__(self):
        self.digitsCharsMap = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        combinations = list()
        self.generateCombinations(0, [], combinations, digits)
        return combinations

    def generateCombinations(self, currIdx, currPath, combinations, digits):
        if len(currPath) == len(digits):
            combinations.append("".join(currPath))
            return

        currDigit = digits[currIdx]
        for ch in self.digitsCharsMap[currDigit]:
            currPath.append(ch)
            self.generateCombinations(currIdx + 1, currPath, combinations, digits)
            currPath.pop()

        return
