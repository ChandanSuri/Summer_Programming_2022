class Solution(object):
    # This solution has O(MN) time & O(min(MN)) space complexity because of the BFS implementation.
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        numRows = len(grid)
        numCols = len(grid[0])
        numIslands = 0

        for idx in range(numRows):
            for jdx in range(numCols):
                if grid[idx][jdx] == "1":
                    numIslands += 1
                    neighbors = list()
                    neighbors.append(idx * numCols + jdx)
                    grid[idx][jdx] = "0"

                    while len(neighbors) != 0:
                        currElem = neighbors.pop(0)
                        currRowIdx = currElem // numCols
                        currColIdx = currElem % numCols

                        if currRowIdx - 1 >= 0 and grid[currRowIdx - 1][currColIdx] == "1":
                            neighbors.append((currRowIdx - 1) * numCols + currColIdx)
                            grid[currRowIdx - 1][currColIdx] = "0"
                        if currColIdx - 1 >= 0 and grid[currRowIdx][currColIdx - 1] == "1":
                            neighbors.append(currRowIdx * numCols + currColIdx - 1)
                            grid[currRowIdx][currColIdx - 1] = "0"
                        if currRowIdx + 1 < numRows and grid[currRowIdx + 1][currColIdx] == "1":
                            neighbors.append((currRowIdx + 1) * numCols + currColIdx)
                            grid[currRowIdx + 1][currColIdx] = "0"
                        if currColIdx + 1 < numCols and grid[currRowIdx][currColIdx + 1] == "1":
                            neighbors.append(currRowIdx * numCols + currColIdx + 1)
                            grid[currRowIdx][currColIdx + 1] = "0"

        return numIslands
