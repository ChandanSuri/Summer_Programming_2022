class Solution(object):
    # This solution is O(n) time and O(1) space
    # Based on Fibonacci Sequence
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1 or n == 2:
            return n

        prev_step1 = 1
        prev_step2 = 2

        for curr_step in range(3, n + 1):
            num_ways = prev_step1 + prev_step2
            prev_step1 = prev_step2
            prev_step2 = num_ways

        return num_ways
