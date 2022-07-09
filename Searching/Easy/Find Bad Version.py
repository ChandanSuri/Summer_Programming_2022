# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        leftVersion = 1
        rightVersion = n

        while leftVersion < rightVersion:
            midVersion = leftVersion + (rightVersion - leftVersion) // 2
            if isBadVersion(midVersion):
                rightVersion = midVersion
            else:
                leftVersion = midVersion + 1

        return rightVersion
