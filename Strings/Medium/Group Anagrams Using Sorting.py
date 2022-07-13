import collections

class Solution(object):
    # O(NKlogK) time and O(NK) space
    # where N is the number of anagrams given and K is the maximum length of any anagram
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)

        for currStr in strs:
            groups[tuple(sorted(currStr))].append(currStr)

        return groups.values()
