from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groupedHashedAnagrams = defaultdict(list)

        for currStr in strs:
            counts = [0] * 26
            for currChar in currStr:
                counts[ord(currChar) - ord('a')] += 1
            groupedHashedAnagrams[tuple(counts)].append(currStr)

        return groupedHashedAnagrams.values()