# O(LogN) time and O(1) space
# Iterative Solution
def binarySearch(array, target):
    startIdx = 0
    endIdx = len(array) - 1

    while startIdx <= endIdx:
        midIdx = startIdx + (endIdx - startIdx) // 2
        if array[midIdx] == target:
            return midIdx
        elif array[midIdx] > target:
            endIdx = midIdx - 1
        else:
            startIdx = midIdx + 1

    return -1


# Recursive solution
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, startIdx, endIdx):
    if startIdx > endIdx:
        return -1

    midIdx = startIdx + (endIdx - startIdx) // 2
    if array[midIdx] == target:
        return midIdx
    elif array[midIdx] > target:
        binarySearchHelper(array, target, startIdx, midIdx - 1)
    else:
        binarySearchHelper(array, target, midIdx + 1, endIdx)
