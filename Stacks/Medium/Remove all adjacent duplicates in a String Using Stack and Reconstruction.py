class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        str_ls = list(s)
        count_chars = [1]
        idx = 1

        while idx < len(str_ls):
            prev_char = str_ls[idx - 1] if len(count_chars) != 0 else ''
            curr_char = str_ls[idx]
            if curr_char != prev_char:
                count_chars.append(1)
            else:
                count_chars[len(count_chars) - 1] += 1
                if count_chars[len(count_chars) - 1] == k:
                    del str_ls[idx - k + 1: idx + 1]
                    count_chars.pop(len(count_chars) - 1)
                    idx = idx - k
            idx += 1

        return ''.join(str_ls)
