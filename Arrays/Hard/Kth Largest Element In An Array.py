import random


class Solution(object):
    # This is the Quick Select algorithm based on the Quick Sort algorithm.
    # But, here we don't sort the whole array we take subset of the array in each iteration.
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        startIdx = 0
        endIdx = len(nums) - 1
        kthSmallest = len(nums) - k

        return self.quickSelect(nums, startIdx, endIdx, kthSmallest)

    def quickSelect(self, nums, startIdx, endIdx, kthSmallest):
        if startIdx == endIdx:
            return nums[startIdx]

        pivotIdx = self.partition(nums, startIdx, endIdx, random.randint(startIdx, endIdx))
        if kthSmallest < pivotIdx:
            return self.quickSelect(nums, startIdx, pivotIdx - 1, kthSmallest)
        elif kthSmallest > pivotIdx:
            return self.quickSelect(nums, pivotIdx + 1, endIdx, kthSmallest)
        else:
            return nums[kthSmallest]

    def partition(self, nums, startIdx, endIdx, pivotIdx):
        pivot = nums[pivotIdx]
        nums[pivotIdx], nums[endIdx] = nums[endIdx], nums[pivotIdx]

        prevSmallIdx = startIdx
        for idx in range(startIdx, endIdx):
            if nums[idx] < pivot:
                nums[idx], nums[prevSmallIdx] = nums[prevSmallIdx], nums[idx]
                prevSmallIdx += 1

        nums[endIdx], nums[prevSmallIdx] = nums[prevSmallIdx], nums[endIdx]

        return prevSmallIdx
