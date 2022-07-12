class Solution(object):
    # This algorithm is O(n) time and O(1) space
    # We convert the problem of incrementing to decrementing
    # and just calculate the minimum value at first.
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        moves = 0
        minValue = min(nums)

        for idx in range(len(nums)):
            moves += (nums[idx] - minValue)

        return moves
