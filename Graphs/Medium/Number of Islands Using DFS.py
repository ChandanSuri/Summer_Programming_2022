class Solution(object):
    # This solution has O(MN) time & O(MN) space complexity
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        numIslands = 0

        for idx in range(len(grid)):
            for jdx in range(len(grid[0])):
                if grid[idx][jdx] == "1":
                    self.dfs(grid, idx, jdx)
                    numIslands += 1

        return numIslands

    def dfs(self, grid, currRow, currCol):
        if currRow < 0 or currCol < 0 or currRow >= len(grid) \
                or currCol >= len(grid[0]) or grid[currRow][currCol] == "0":
            return

        grid[currRow][currCol] = "0"
        self.dfs(grid, currRow - 1, currCol)
        self.dfs(grid, currRow, currCol - 1)
        self.dfs(grid, currRow + 1, currCol)
        self.dfs(grid, currRow, currCol + 1)
