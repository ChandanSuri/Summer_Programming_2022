class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftIdx = 0
        rightIdx = len(nums) - 1

        while leftIdx < rightIdx:
            midIdx = leftIdx + (rightIdx - leftIdx) // 2
            if nums[midIdx] > nums[midIdx + 1]:
                rightIdx = midIdx
            else:
                leftIdx = midIdx + 1

        return leftIdx
