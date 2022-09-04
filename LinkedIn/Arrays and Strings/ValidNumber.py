class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seenDigit = False
        seenExponent = False
        seenDot = False

        for idx, ch in enumerate(s):
            if ch.isdigit():
                seenDigit = True
            elif ch in ["+", "-"]:
                if idx > 0 and s[idx - 1] != 'e' and s[idx - 1] != 'E':
                    return False
            elif ch in ["e", "E"]:
                if seenExponent or not seenDigit:
                    return False
                seenExponent = True
                seenDigit = False
            elif ch == ".":
                if seenDot or seenExponent:
                    return False
                seenDot = True
            else:
                return False

        return seenDigit
