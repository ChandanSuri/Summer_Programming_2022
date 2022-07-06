class Solution(object):
    # This solution is constant time and space as we are just calculating the same through a formula.
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        sqrt_val = 5 ** (1.0 / 2.0)
        phi = (1 + sqrt_val) / 2
        psi = (1 - sqrt_val) / 2

        return int(round((phi ** (n + 1) - psi ** (n + 1)) / sqrt_val))
