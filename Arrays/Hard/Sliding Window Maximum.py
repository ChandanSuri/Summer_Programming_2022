class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        len_nums = len(nums)
        if len_nums == 0 or k == 0:
            return []
        if k == 1:
            return nums

        left = [0] * len_nums
        right = [0] * len_nums
        left[0] = nums[0]
        right[-1] = nums[-1]

        for idx in range(1, len_nums):
            if idx % k == 0:
                left[idx] = nums[idx]
            else:
                left[idx] = max(left[idx - 1], nums[idx])

        for jdx in range(len_nums - 2, -1, -1):
            if (jdx + 1) % k == 0:
                right[jdx] = nums[jdx]
            else:
                right[jdx] = max(right[jdx + 1], nums[jdx])

        max_values = []
        for idx in range(len_nums - k + 1):
            max_values.append(max(left[idx + k - 1], right[idx]))

        return max_values
