class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """

        if len(sentence) < 26:
            return False

        charsPresent = set()

        for char in sentence:
            charsPresent.add(char)

        return True if len(charsPresent) == 26 else False
