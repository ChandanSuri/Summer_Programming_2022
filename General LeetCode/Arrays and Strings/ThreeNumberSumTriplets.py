class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lenNums = len(nums)
        nums.sort()
        triplets = list()

        for idx in range(lenNums):
            startIdx = idx + 1
            endIdx = lenNums - 1

            if idx != 0 and nums[idx] == nums[idx - 1]:
                continue

            while startIdx < endIdx:
                currSum = nums[idx] + nums[startIdx] + nums[endIdx]
                if currSum < 0:
                    startIdx += 1
                elif currSum > 0:
                    endIdx -= 1
                else:
                    triplets.append([nums[idx], nums[startIdx], nums[endIdx]])
                    startIdx += 1
                    endIdx -= 1

                    while startIdx < endIdx and nums[startIdx] == nums[startIdx - 1]:
                        startIdx += 1

        return triplets
