class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        items.sort(key=lambda item: (item[0], -item[1]))
        high_fives = list()
        prev_id = items[0][0]
        curr_count = accum_score = 0

        for item in items:
            curr_id = item[0]
            curr_score = item[1]

            if curr_id != prev_id:
                curr_count = 0
                accum_score = 0
                prev_id = curr_id

            curr_count += 1
            accum_score += curr_score

            if curr_count > 5:
                continue
            elif curr_count == 5:
                high_fives.append([curr_id, int(accum_score / 5.0)])

        return high_fives
