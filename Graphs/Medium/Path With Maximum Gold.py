class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxGold = 0

        for startCoordX in range(len(grid)):
            for startCoordY in range(len(grid[0])):
                maxGoldInWalk = [0]
                if grid[startCoordX][startCoordY] != 0:
                    self.walkThroughMine(grid, startCoordX, startCoordY, 0, maxGoldInWalk)
                    if maxGoldInWalk[0] > maxGold:
                        maxGold = maxGoldInWalk[0]

        return maxGold

    def walkThroughMine(self, grid, currCoordX, currCoordY, goldCollected, maxGoldInWalk):
        xLen = len(grid)
        yLen = len(grid[0])

        currGold = grid[currCoordX][currCoordY]
        goldCollected += currGold
        grid[currCoordX][currCoordY] = 0
        if goldCollected > maxGoldInWalk[0]:
            maxGoldInWalk[0] = goldCollected

        if currCoordX + 1 < xLen and grid[currCoordX + 1][currCoordY] != 0:
            self.walkThroughMine(grid, currCoordX + 1, currCoordY, goldCollected, maxGoldInWalk)
        if currCoordY + 1 < yLen and grid[currCoordX][currCoordY + 1] != 0:
            self.walkThroughMine(grid, currCoordX, currCoordY + 1, goldCollected, maxGoldInWalk)
        if currCoordX - 1 >= 0 and grid[currCoordX - 1][currCoordY] != 0:
            self.walkThroughMine(grid, currCoordX - 1, currCoordY, goldCollected, maxGoldInWalk)
        if currCoordY - 1 >= 0 and grid[currCoordX][currCoordY - 1] != 0:
            self.walkThroughMine(grid, currCoordX, currCoordY - 1, goldCollected, maxGoldInWalk)

        grid[currCoordX][currCoordY] = currGold

        return
