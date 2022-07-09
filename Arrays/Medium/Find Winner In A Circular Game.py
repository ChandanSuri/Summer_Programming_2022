class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        players = [idx for idx in range(1, n + 1)]
        currIdx = 0

        while len(players) > 1:
            currIdx = (currIdx + k - 1) % len(players)
            players.pop(currIdx)
            currIdx = currIdx % len(players)

        return players[0]
