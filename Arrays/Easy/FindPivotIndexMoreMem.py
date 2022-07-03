class Solution(object):
    # O(N) time and O(N) space
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)

        left_sums_arr = [-1] * nums_len
        left_running_sum = 0
        for idx in range(nums_len):
            left_sums_arr[idx] = left_running_sum
            left_running_sum += nums[idx]

        right_sums_arr = [-1] * nums_len
        right_running_sum = 0
        for idx in range(nums_len - 1, -1, -1):
            right_sums_arr[idx] = right_running_sum
            right_running_sum += nums[idx]

        for idx in range(nums_len):
            if left_sums_arr[idx] == right_sums_arr[idx]:
                return idx

        return -1
