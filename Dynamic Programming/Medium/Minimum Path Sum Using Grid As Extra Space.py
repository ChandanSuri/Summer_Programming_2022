class Solution(object):
    # This is O(mn) time and O(mn) space complexity. (Using Grid as an extra space)
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_rows = len(grid)
        num_cols = len(grid[0])
        min_sums = [[0] * num_cols] * num_rows

        for idx in range(num_rows - 1, -1, -1):
            for jdx in range(num_cols - 1, -1, -1):
                if idx != num_rows - 1 and jdx != num_cols - 1:
                    min_sums[idx][jdx] = grid[idx][jdx] + min(min_sums[idx][jdx + 1], min_sums[idx + 1][jdx])
                elif idx == num_rows - 1 and jdx != num_cols - 1:
                    min_sums[idx][jdx] = grid[idx][jdx] + min_sums[idx][jdx + 1]
                elif idx != num_rows - 1 and jdx == num_cols - 1:
                    min_sums[idx][jdx] = grid[idx][jdx] + min_sums[idx + 1][jdx]
                else:
                    min_sums[idx][jdx] = grid[idx][jdx]

        return min_sums[0][0]
