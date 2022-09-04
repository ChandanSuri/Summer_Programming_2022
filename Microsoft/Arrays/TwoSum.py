class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        elemToIdxMap = dict()

        for idx, elem in enumerate(nums):
            if target - elem in elemToIdxMap:
                return [elemToIdxMap[target - elem], idx]
            elemToIdxMap[elem] = idx

        return [-1, -1]
