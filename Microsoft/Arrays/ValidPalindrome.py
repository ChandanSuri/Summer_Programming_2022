class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.upper()
        formattedStr = list()
        for ch in s:
            if (65 <= ord(ch) <= 90) or (48 <= ord(ch) <= 57):
                formattedStr.append(ch)

        formattedStr = "".join(formattedStr)
        currIdx = 0
        lenStr = len(formattedStr)

        while currIdx < lenStr // 2:
            if formattedStr[currIdx] != formattedStr[lenStr - 1 - currIdx]:
                return False
            currIdx += 1

        return True
