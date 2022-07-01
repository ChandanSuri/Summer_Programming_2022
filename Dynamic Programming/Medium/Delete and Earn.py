class Solution(object):
    def __init__(self):
        self.points = dict()
        self.cache = dict()

    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0

        for num in nums:
            self.points[num] = self.points.get(num, 0) + num
            max_num = max(max_num, num)

        return self.maxEarning(max_num)

    def maxEarning(self, curr_num):
        if curr_num == 0 or curr_num not in self.points:
            return 0
        if curr_num == 1:
            return self.points[1]

        if curr_num in self.cache:
            return self.cache.get(curr_num)

        self.cache[curr_num] = max(self.maxEarning(curr_num - 1),
                                   self.maxEarning(curr_num - 2) + self.points[curr_num])

        return self.cache[curr_num]
