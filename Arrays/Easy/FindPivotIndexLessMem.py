class Solution(object):
    # O(N) time and O(1) space
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total_sum = sum(nums)
        left_running_sum = 0
        for idx, num in enumerate(nums):
            if left_running_sum == total_sum - left_running_sum - num:
                return idx
            left_running_sum += num

        return -1
