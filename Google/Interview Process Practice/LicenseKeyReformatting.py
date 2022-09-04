class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        formattedStr = s.upper().replace('-', '')
        lenFormattedStr = len(formattedStr)
        remainder = k if lenFormattedStr % k == 0 else lenFormattedStr % k
        licenseKeyReformatted = list()
        licenseKeyReformatted.append(formattedStr[:remainder])
        currIdx = remainder

        while currIdx < lenFormattedStr:
            licenseKeyReformatted.append(formattedStr[currIdx: currIdx + k])
            currIdx += k

        return "-".join(licenseKeyReformatted)
