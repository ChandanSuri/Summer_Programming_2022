class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        numCoins = len(coins)
        numWaysForAmounts = [0] * (amount + 1)
        numWaysForAmounts[0] = 1

        for coin in coins:
            for currAmount in range(coin, amount + 1):
                numWaysForAmounts[currAmount] += numWaysForAmounts[currAmount - coin]

        return numWaysForAmounts[-1]
