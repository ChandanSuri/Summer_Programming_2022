class Solution(object):
    # This is an O(n) time and O(n) space solution.
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = dict()
        num_possibilities = self.climbStairsHelper(0, n, cache)
        return num_possibilities

    def climbStairsHelper(self, curr_step, n, cache):
        if curr_step > n:
            return 0

        if curr_step == n:
            return 1

        if curr_step in cache:
            return cache[curr_step]

        cache[curr_step] = self.climbStairsHelper(curr_step + 1, n, cache) + self.climbStairsHelper(curr_step + 2, n, cache)

        return cache[curr_step]