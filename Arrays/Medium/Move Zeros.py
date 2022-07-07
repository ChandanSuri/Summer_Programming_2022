class Solution(object):
    # This is a linear time and constant space solution.
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        prev_idx = -1
        for idx in range(len(nums)):
            if nums[idx] == 0:
                prev_idx = idx
                break

        if prev_idx == -1:
            return nums

        curr_idx = prev_idx + 1
        while curr_idx < len(nums):
            if nums[curr_idx] != 0:
                nums[prev_idx], nums[curr_idx] = nums[curr_idx], nums[prev_idx]
                prev_idx += 1
            curr_idx += 1

        return nums
