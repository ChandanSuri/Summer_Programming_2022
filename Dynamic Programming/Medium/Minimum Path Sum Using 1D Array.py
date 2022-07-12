class Solution(object):
    # This is O(mn) time and O(n) space complexity. (using a 1D Array)
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_rows = len(grid)
        num_cols = len(grid[0])
        min_sums = [0] * num_cols

        for idx in range(num_rows - 1, -1, -1):
            for jdx in range(num_cols - 1, -1, -1):
                if idx != num_rows - 1 and jdx != num_cols - 1:
                    min_sums[jdx] = grid[idx][jdx] + min(min_sums[jdx + 1], min_sums[jdx])
                elif idx == num_rows - 1 and jdx != num_cols - 1:
                    min_sums[jdx] = grid[idx][jdx] + min_sums[jdx + 1]
                elif idx != num_rows - 1 and jdx == num_cols - 1:
                    min_sums[jdx] = grid[idx][jdx] + min_sums[jdx]
                else:
                    min_sums[jdx] = grid[idx][jdx]

        return min_sums[0]
