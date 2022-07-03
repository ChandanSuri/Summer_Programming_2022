class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float("inf")
        max_profit = 0

        for idx in range(len(prices)):
            curr_price = prices[idx]
            if curr_price < min_price:
                min_price = curr_price
            elif curr_price - min_price > max_profit:
                max_profit = curr_price - min_price

        return max_profit
