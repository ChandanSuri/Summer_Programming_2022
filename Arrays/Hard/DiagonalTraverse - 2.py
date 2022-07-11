class Solution(object):
    # O(n*m) time and O(1) space complexity
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        num_rows = len(mat)
        num_cols = len(mat[0])
        result = list()
        # True value suggests upward direction and False suggests downward direction of the diagonal.
        direction = True
        start_row_idx = start_col_idx = 0

        while start_row_idx < num_rows and start_col_idx < num_cols:
            curr_row_idx = start_row_idx
            curr_col_idx = start_col_idx

            # Iterating over the current diagonal according to the direction
            while 0 <= curr_row_idx < num_rows and num_cols > curr_col_idx >= 0:
                result.append(mat[curr_row_idx][curr_col_idx])
                if direction:
                    curr_row_idx -= 1
                    curr_col_idx += 1
                else:
                    curr_row_idx += 1
                    curr_col_idx -= 1

            # Update the starting positions for the next diagonal
            if direction:
                if start_col_idx == num_cols - 1:
                    start_row_idx = curr_row_idx
                    start_col_idx = curr_col_idx
                else:
                    start_col_idx = curr_col_idx
                    start_row_idx = curr_row_idx + 1
            else:
                if start_row_idx == num_rows - 1:
                    start_col_idx = curr_col_idx
                    start_row_idx = curr_row_idx
                else:
                    start_row_idx = curr_row_idx
                    start_col_idx = curr_col_idx + 1

            # Update the direction for the next diagonal
            direction = not direction

        return result

