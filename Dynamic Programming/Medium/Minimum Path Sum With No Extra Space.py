class Solution(object):
    # This is O(mn) time and O(1) space complexity.
    # NOTE: This is assuming that we can change the original 2D Array provided.
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_rows = len(grid)
        num_cols = len(grid[0])

        for idx in range(num_rows - 1, -1, -1):
            for jdx in range(num_cols - 1, -1, -1):
                if idx != num_rows - 1 and jdx != num_cols - 1:
                    grid[idx][jdx] += min(grid[idx][jdx + 1], grid[idx + 1][jdx])
                elif idx == num_rows - 1 and jdx != num_cols - 1:
                    grid[idx][jdx] += grid[idx][jdx + 1]
                elif idx != num_rows - 1 and jdx == num_cols - 1:
                    grid[idx][jdx] += grid[idx + 1][jdx]

        return grid[0][0]