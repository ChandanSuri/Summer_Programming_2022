class Solution(object):
    # This is a O(n) solution which uses constant space.
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lenNums = len(numbers)
        leftIdx = 0
        rightIdx = lenNums - 1

        while leftIdx < rightIdx:
            potentialTarget = numbers[leftIdx] + numbers[rightIdx]
            if potentialTarget < target:
                leftIdx += 1
            elif potentialTarget > target:
                rightIdx -= 1
            else:
                return [leftIdx + 1, rightIdx + 1]

        return [-1, -1]
