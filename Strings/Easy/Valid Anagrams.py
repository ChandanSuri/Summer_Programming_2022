class Solution(object):
    # This is a linear time and constant space solution (can at most have 26 keys)
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        alphabets_dict = dict()

        for char in s:
            alphabets_dict[char] = alphabets_dict.get(char, 0) + 1

        for char in t:
            alphabets_dict[char] = alphabets_dict.get(char, 0) - 1
            if alphabets_dict[char] < 0:
                return False

        for _, count in alphabets_dict.items():
            if count != 0:
                return False

        return True
