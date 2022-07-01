class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        # This is a O (n*n) time algorithm with O(1) space complexity

        num_ratings = len(rating)
        num_teams = 0

        for curr_idx in range(num_ratings):
            curr_rating = rating[curr_idx]
            left_inc_nums = left_dec_nums = right_inc_nums = right_dec_nums = 0

            for left_rating in rating[:curr_idx]:
                if left_rating < curr_rating:
                    left_inc_nums += 1
                elif left_rating > curr_rating:
                    left_dec_nums += 1

            for right_rating in rating[curr_idx:]:
                if right_rating < curr_rating:
                    right_dec_nums += 1
                elif right_rating > curr_rating:
                    right_inc_nums += 1

            num_teams += (left_inc_nums * right_inc_nums) + (left_dec_nums * right_dec_nums)

        return num_teams
