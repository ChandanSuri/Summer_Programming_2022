class Solution(object):
    # This is a linear time and constant space solution
    # (as dictionary has constant number of values)
    # Also, we go from left to right in this solution!
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Initial Data
        possible_symbol_vals_map = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }

        # Logic
        final_num = 0
        roman_length = len(s)
        idx = 0
        while idx < roman_length:
            if idx + 1 < roman_length and s[idx: idx + 2] in possible_symbol_vals_map:
                final_num += possible_symbol_vals_map[s[idx: idx + 2]]
                idx += 1
            else:
                final_num += possible_symbol_vals_map[s[idx]]
            idx += 1

        return final_num
