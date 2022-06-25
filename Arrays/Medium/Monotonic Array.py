def isMonotonic(array):
    isIncreasing = True
    isDecreasing = True

    for idx in range(len(array) - 1):
        currElement = array[idx]
        nextElement = array[idx + 1]
        if currElement > nextElement:
            isIncreasing = False
        elif currElement < nextElement:
            isDecreasing = False

    return isIncreasing or isDecreasing
