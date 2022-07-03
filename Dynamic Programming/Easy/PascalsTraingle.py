class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        result = list()

        for rowNum in range(numRows):
            rowData = [None for _ in range(rowNum + 1)]
            rowData[0] = rowData[-1] = 1

            for rowIdx in range(1, len(rowData) - 1):
                rowData[rowIdx] = result[rowNum - 1][rowIdx - 1] + result[rowNum - 1][rowIdx]

            result.append(rowData)

        return result
