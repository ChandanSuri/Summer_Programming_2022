class Solution(object):
    # This is a O(n) solution which consumes O(n) space as strings are immutable in python.
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        strLen = len(palindrome)

        if strLen <= 1:
            return ""

        strArr = list(palindrome)
        idx = 0

        while idx < strLen // 2:
            currChar = palindrome[idx]
            if currChar != 'a':
                strArr[idx] = 'a'
                break
            idx += 1
        if idx == strLen // 2:
            strArr[strLen - 1] = 'b'

        return ''.join(strArr)
