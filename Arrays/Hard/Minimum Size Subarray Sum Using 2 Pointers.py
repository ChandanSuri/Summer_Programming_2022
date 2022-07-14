class Solution(object):
    # This algorithm runs in O(n) time and O(1) space
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minLen = float("inf")
        leftIdx = 0
        currRunningSum = 0

        for currIdx in range(len(nums)):
            currRunningSum += nums[currIdx]
            while currRunningSum >= target:
                minLen = min(minLen, currIdx + 1 - leftIdx)
                currRunningSum -= nums[leftIdx]
                leftIdx += 1

        return minLen if minLen != float("inf") else 0
