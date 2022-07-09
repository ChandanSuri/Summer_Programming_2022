class Solution(object):
    def __init__(self):
        self.perms = list()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.backtrack(0, nums)

        return self.perms

    def backtrack(self, currElemIdx, nums):
        n = len(nums)

        if currElemIdx == n:
            self.perms.append(nums[:])

        for idx in range(currElemIdx, n):
            nums[currElemIdx], nums[idx] = nums[idx], nums[currElemIdx]
            self.backtrack(currElemIdx + 1, nums)
            nums[idx], nums[currElemIdx] = nums[currElemIdx], nums[idx]

        return
