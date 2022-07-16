class Solution(object):
    # This is an O(n) time solution with O(1) space complexity
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftIdx = 0
        rightIdx = len(height) - 1
        maxArea = 0

        while leftIdx < rightIdx:
            maxArea = max(maxArea, min(height[leftIdx], height[rightIdx]) * (rightIdx - leftIdx))
            if height[leftIdx] <= height[rightIdx]:
                leftIdx += 1
            else:
                rightIdx -= 1

        return maxArea
