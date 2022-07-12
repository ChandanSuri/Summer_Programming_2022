class Solution(object):
    # This algorithm is O(nlogn) time as we do sorting and O(1) space
    # Also, we increment the array values in bursts.
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        moves = 0

        for idx in range(len(nums) - 1, -1, -1):
            moves += (nums[idx] - nums[0])

        return moves
