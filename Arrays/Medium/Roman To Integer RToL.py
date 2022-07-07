class Solution(object):
    # This is a linear time and constant space solution
    # (as dictionary has constant number of values)
    # Also, we go from right to left in this solution!
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Initial Data
        possible_symbol_vals_map = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }

        # Logic
        final_num = 0
        roman_length = len(s)
        idx = roman_length - 1
        while idx >= 0:
            roman_numeral = s[idx]
            if idx + 1 < roman_length and possible_symbol_vals_map[roman_numeral] < possible_symbol_vals_map[s[idx + 1]]:
                final_num -= possible_symbol_vals_map[roman_numeral]
            else:
                final_num += possible_symbol_vals_map[roman_numeral]
            idx -= 1

        return final_num
