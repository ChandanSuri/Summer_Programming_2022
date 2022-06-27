# O(N) time and O(1) space
def firstDuplicateValue(array):
    idx = 0
    while idx < len(array):
        currValue = array[idx]
        nextIdx = abs(currValue) - 1
        if array[nextIdx] < 0:
            return abs(currValue)
        array[nextIdx] *= -1
        idx += 1

    return -1
