class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        charMap = dict()

        for char in s:
            charMap[char] = charMap.get(char, 0) + 1

        for idx, char in enumerate(s):
            if charMap[char] == 1:
                return idx

        return -1
