# This program has 2 versions of code:

# First one with more lines of code:

# O(N) time and O(N) space
def checkForExtremes(array, leftIdx, rightIdx):
    leftSqrElem = rightSqrElem = float("inf")
    if leftIdx >= 0:
        leftSqrElem = array[leftIdx]**2
    if rightIdx < len(array):
        rightSqrElem = array[rightIdx]**2

    return leftSqrElem, rightSqrElem


def sortedSquaredArray(array):
    rightIdx = 0
    while rightIdx < len(array) and array[rightIdx] < 0:
        rightIdx += 1

    leftIdx = rightIdx - 1
    resultsArr = []

    while rightIdx - leftIdx <= len(array):
        leftSqrElem, rightSqrElem = checkForExtremes(array, leftIdx, rightIdx)
        if leftSqrElem < rightSqrElem:
            resultsArr.append(leftSqrElem)
            leftIdx -= 1
        else:
            resultsArr.append(rightSqrElem)
            rightIdx += 1

    return resultsArr


# Second Version is as follows:
def sortedSquaredArray(array):
    leftIdx = 0
    rightIdx = resultsIdx = len(array) - 1
    resultsArr = [0] * len(array)

    while resultsIdx >= 0:
        leftElem = array[leftIdx]
        rightElem = array[rightIdx]

        if abs(leftElem) > abs(rightElem):
            resultsArr[resultsIdx] = leftElem**2
            leftIdx += 1
        else:
            resultsArr[resultsIdx] = rightElem**2
            rightIdx -= 1
        resultsIdx -= 1

    return resultsArr

