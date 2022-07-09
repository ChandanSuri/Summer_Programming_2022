class Solution(object):
    # O(n*m) time and O(min(n, m)) space complexity
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        num_rows = len(mat)
        num_cols = len(mat[0])
        total_diagonals = num_rows + num_cols - 1
        start_row_idx = start_col_idx = 0
        result = list()

        for diag_idx in range(total_diagonals):
            # Each time, we would need a new intermediate list
            # in order to store current diagonal elements.
            intermediate_arr = list()
            curr_row_idx = start_row_idx
            curr_col_idx = start_col_idx

            # Iterating over the current diagonal
            while curr_row_idx < num_rows and curr_col_idx >= 0:
                intermediate_arr.append(mat[curr_row_idx][curr_col_idx])
                curr_row_idx += 1
                curr_col_idx -= 1

            # Diagonal index decides the direction, when needs to be reversed or not!
            if diag_idx % 2 == 0:
                result.extend(intermediate_arr[::-1])
            else:
                result.extend(intermediate_arr)

            # Next starting position decision (for next diagonal)
            if start_col_idx == (num_cols - 1):
                start_row_idx += 1
            else:
                start_col_idx += 1

        return result
    