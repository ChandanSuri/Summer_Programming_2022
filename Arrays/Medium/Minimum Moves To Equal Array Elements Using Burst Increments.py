class Solution(object):
    # This algorithm is O(n**2) time and O(1) space
    # We increment the array values in bursts.
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minIdx = 0
        maxIdx = len(nums) - 1
        moves = 0

        while True:
            # First get the minimum and the maximum element in the array.
            for idx in range(len(nums)):
                if nums[idx] < nums[minIdx]:
                    minIdx = idx
                if nums[idx] > nums[maxIdx]:
                    maxIdx = idx

            # Now all the elements are equal if this condition is satisfied.
            diff = nums[maxIdx] - nums[minIdx]
            if nums[maxIdx] == nums[minIdx]:
                break

            for idx in range(len(nums)):
                if idx != maxIdx:
                    nums[idx] += diff

            moves += diff

        return moves
