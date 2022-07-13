import collections

class Solution(object):
    # This is a O(NK) time and O(NK) space algorithm
    # where N is the number of anagrams and K is the maximum size of the anagrams
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)

        for currStr in strs:
            count = [0] * 26
            for ch in currStr:
                count[ord(ch) - ord('a')] += 1
            groups[tuple(count)].append(currStr)

        return groups.values()
