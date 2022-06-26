# O(N) time and O(1) space
def longestPeak(array):
    idx = 1
    maxPeakSize = 0

    while idx < len(array) - 1:
        prevElem = array[idx - 1]
        currElem = array[idx]
        nextElem = array[idx + 1]

        isPeak = prevElem < currElem and currElem > nextElem
        if not isPeak:
            idx += 1
            continue

        leftIdx = idx - 1
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1

        rightIdx = idx + 1
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        currPeakSize = rightIdx - leftIdx - 1
        maxPeakSize = max(currPeakSize, maxPeakSize)

        idx = rightIdx - 1

    return maxPeakSize
