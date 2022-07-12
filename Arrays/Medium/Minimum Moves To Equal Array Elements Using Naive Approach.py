class Solution(object):
    # This algorithm is O(n**2.k) time and O(1) space
    # where k is the difference between the maximum and the minimum element in the array.
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
            if nums[maxIdx] == nums[minIdx]:
                break

            # Now, we just increment each element of the array by 1 but the max element in the array.
            for idx in range(len(nums)):
                if idx != maxIdx:
                    nums[idx] += 1

            moves += 1

        return moves
