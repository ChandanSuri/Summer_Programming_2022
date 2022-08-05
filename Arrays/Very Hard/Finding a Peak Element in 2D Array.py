class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        startCol = 0
        endCol = len(mat[0]) - 1
        numRows = len(mat)

        while startCol <= endCol:
            maxRow = 0
            midCol = startCol + (endCol - startCol) // 2

            for row in range(numRows):
                if mat[maxRow][midCol] <= mat[row][midCol]:
                    maxRow = row

            leftIsBig = midCol - 1 >= startCol and mat[maxRow][midCol - 1] > mat[maxRow][midCol]
            rightIsBig = midCol + 1 <= endCol and mat[maxRow][midCol + 1] > mat[maxRow][midCol]

            if not leftIsBig and not rightIsBig:
                return [maxRow, midCol]
            elif rightIsBig:
                startCol = midCol + 1
            else:
                endCol = midCol - 1

        return []
