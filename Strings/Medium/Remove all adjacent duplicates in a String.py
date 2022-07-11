class Solution(object):
    # This solution is using Naive approach with just using memoization for the counts of the each character
    # and then reverting back to from where the deletion was done, to be sure that we don't miss cases
    # and thus, don't have to repeatedly go over the same set of characters.
    # Time: O(n) and Space: O(n) complexity.
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        str_ls = list(s)
        count_chars = [0] * len(s)
        count_chars[0] = 1
        idx = 1

        while idx < len(str_ls):
            prev_char = str_ls[idx - 1]
            curr_char = str_ls[idx]
            if curr_char != prev_char:
                count_chars[idx] = 1
            else:
                count_chars[idx] = count_chars[idx - 1] + 1
                if count_chars[idx] == k:
                    del str_ls[idx - k + 1: idx + 1]
                    idx = idx - k

            idx += 1

        return ''.join(str_ls)
