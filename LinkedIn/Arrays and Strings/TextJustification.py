class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        currSetOfWords = list()
        currNumLetters = 0
        result = list()

        for word in words:
            if currNumLetters + len(word) + len(currSetOfWords) > maxWidth:
                if len(currSetOfWords) == 1:
                    result.append(currSetOfWords[0] + ' ' * (maxWidth - currNumLetters))
                else:
                    numSpacesNeeded = maxWidth - currNumLetters
                    spaceBetweenWords, extraSpacesNeeded = divmod(numSpacesNeeded, len(currSetOfWords) - 1)

                    for idx in range(extraSpacesNeeded):
                        currSetOfWords[idx] += ' '

                    result.append((' ' * spaceBetweenWords).join(currSetOfWords))
                currSetOfWords = list()
                currNumLetters = 0

            currSetOfWords.append(word)
            currNumLetters += len(word)

        result.append(' '.join(currSetOfWords) + ' ' * (maxWidth - currNumLetters - len(currSetOfWords) + 1))
        return result
