class Solution(object):
    # This is a linear time and constance space solution.
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        idx1 = idx2 = -1
        minDistance = float("inf")

        for idx, word in enumerate(wordsDict):
            if word == word1:
                idx1 = idx
            elif word == word2:
                idx2 = idx

            if idx1 != -1 and idx2 != -1:
                minDistance = min(minDistance, abs(idx1 - idx2))

        return minDistance
