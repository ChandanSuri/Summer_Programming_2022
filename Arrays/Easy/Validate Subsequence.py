# O(N) time and O(1) space
def isValidSubsequence(array, sequence):
    currIdxInSequence = currIdxInArr = 0

    while currIdxInSequence < len(sequence) and currIdxInArr < len(array):
        if sequence[currIdxInSequence] == array[currIdxInArr]:
            currIdxInSequence += 1
        currIdxInArr += 1

    return currIdxInSequence == len(sequence)