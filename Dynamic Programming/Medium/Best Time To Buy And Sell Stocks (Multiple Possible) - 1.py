class Solution(object):
    # This solution is O(n) time and O(1) space
    # We use peak and valley approach here
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        idx = 0
        maxProfit = 0
        while idx < len(prices) - 1:
            while idx < len(prices) - 1 and prices[idx] >= prices[idx + 1]:
                idx += 1
            valley = prices[idx]
            while idx < len(prices) - 1 and prices[idx] <= prices[idx + 1]:
                idx += 1
            peak = prices[idx]
            maxProfit += peak - valley

        return maxProfit
