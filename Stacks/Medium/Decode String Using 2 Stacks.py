class Solution(object):
    # For this the time complexity is even less!
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        count_stack = []
        string_stack = []
        curr_k = 0
        curr_str = list()

        for char in s:
            if 48 <= ord(char) <= 57:
                curr_k = curr_k * 10 + int(char)
            elif 97 <= ord(char) <= 122:
                curr_str.append(char)
            elif char == '[':
                count_stack.append(curr_k)
                string_stack.append(''.join(curr_str))
                curr_k = 0
                curr_str = list()
            else:
                # This is the case when a closing square bracket is found
                curr_num_repeats = count_stack.pop(len(count_stack) - 1)
                prev_str = string_stack.pop(len(string_stack) - 1)
                repeated_str = [prev_str]
                curr_str = ''.join(curr_str)
                for idx in range(curr_num_repeats):
                    repeated_str.append(curr_str)
                curr_str = repeated_str

        return ''.join(curr_str)
