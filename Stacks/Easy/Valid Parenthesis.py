class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = list()
        leftBracksMap = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack.append(s[0])
        idx = 1

        while idx < len(s):
            currentBrack = s[idx]

            if currentBrack in leftBracksMap:
                stack.append(currentBrack)
            else:
                stackTopBrack = stack.pop(len(stack) - 1) if len(stack) != 0 else '-'
                if leftBracksMap.get(stackTopBrack, '-') != currentBrack:
                    break

            idx += 1

        return len(stack) == 0 and idx == len(s)
