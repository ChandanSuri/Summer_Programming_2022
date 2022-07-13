class Solution(object):
    # This solution is O(n) time and O(1) space
    # We use peak and valley approach here
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0

        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx - 1]:
                maxProfit += prices[idx] - prices[idx - 1]

        return maxProfit
