class Solution(object):
    # This algorithm is O(maxK^countk*n) and maximum value of the decoded string separately.
    # Not quite good complexity... Can be immproved!
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr_k = 0

        for char in s:
            if 48 <= ord(char) <= 57:
                curr_k = curr_k * 10 + int(char)
            elif char == '[':
                stack.append(curr_k)
                curr_k = 0
                stack.append(char)
            elif 97 <= ord(char) <= 122:
                stack.append(char)
            else:
                # When char is the square closing bracket
                curr_chars = list()
                while stack[-1] != '[':
                    curr_chars.append(stack.pop(len(stack) - 1))
                curr_chars.reverse()
                curr_chars = ''.join(curr_chars)
                del stack[-1]
                num_repeats = stack.pop(len(stack) - 1)
                strs = list()
                for idx in range(num_repeats):
                    strs.append(curr_chars)
                repeated_str = ''.join(strs)
                stack.append(repeated_str)

        decoded_str = ''.join(stack)

        return decoded_str
