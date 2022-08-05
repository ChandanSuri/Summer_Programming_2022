class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumsCountMap = dict()
        lenNums = len(nums)
        sumsCountMap[0] = 1
        runningSum = 0
        count = 0

        for idx in range(lenNums):
            runningSum += nums[idx]
            if (runningSum - k) in sumsCountMap:
                count += sumsCountMap[runningSum - k]
            sumsCountMap[runningSum] = sumsCountMap.get(runningSum, 0) + 1

        return count
