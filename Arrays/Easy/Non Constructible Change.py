"""
NOTES:
1. When you need to extract some information which is easily extractable
when a sorted array is provided, sort the array first. Might not be the best
solution but always helps in reducing the complexity of the problem.
2. You can use intermediary data in order to help you find the next entry in
your result.
3. For math problems like this one, consider getting the data in an ordered
fashion and then use that implicit ordering of the data to your advantage!
"""


# O(NlogN) time and O(1) space
def nonConstructibleChange(coins):
    # Sorting the coins would help us efficiently solve this inherently exponential problem
    coins.sort()
    runningSum = 0

    for coin in coins:
        '''
        If the current coin is at least greater by 2 from the running sum, that would mean that we cannot create
        runningSum + 1 value as running sum means that a value less than or equal to the running sum could be created
        with the coins before the current one and if the current coin is greater than that sum by more than 1, then
        we would surely miss a value that cannot be created with the current set of coins.
        '''
        if coin > runningSum + 1:
            break
        runningSum += coin

    return runningSum + 1
