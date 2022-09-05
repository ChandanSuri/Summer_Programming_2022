class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        numFruits = len(fruits)

        if numFruits in [1, 2]:
            return numFruits

        prevIdx1 = 0
        prevIdx2 = 1
        while prevIdx2 < numFruits:
            if fruits[prevIdx2] != fruits[prevIdx1]:
                break
            prevIdx2 += 1
        currIdx = prevIdx2 + 1
        currMaxFruits = maxFruits = prevIdx2 - prevIdx1 + 1 if prevIdx2 != numFruits else numFruits
        prevIdx1 = prevIdx2 - 1

        while currIdx < len(fruits):
            if fruits[currIdx] == fruits[prevIdx1]:
                prevIdx1 = currIdx
                currMaxFruits += 1
            elif fruits[currIdx] == fruits[prevIdx2]:
                prevIdx2 = currIdx
                currMaxFruits += 1
            else:
                maxFruits = max(maxFruits, currMaxFruits)

                if prevIdx1 == currIdx - 1:
                    currMaxFruits = currIdx - prevIdx2
                    prevIdx2 = currIdx
                elif prevIdx2 == currIdx - 1:
                    currMaxFruits = currIdx - prevIdx1
                    prevIdx1 = currIdx

            currIdx += 1

        return max(maxFruits, currMaxFruits)
