class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        columnTitle = list()

        while columnNumber > 0:
            currCharNum = (columnNumber - 1) % 26
            columnNumber = (columnNumber - 1) // 26
            columnTitle.insert(0, chr(ord('A') + currCharNum))

        return ''.join(columnTitle)
