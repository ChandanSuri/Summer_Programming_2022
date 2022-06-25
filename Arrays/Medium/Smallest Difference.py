def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    arrayOnePtr = arrayTwoPtr = 0
    minDiff = float("inf")
    result = [float("inf"), float("inf")]

    while arrayOnePtr < len(arrayOne) and arrayTwoPtr < len(arrayTwo):
        arrayOneEle = arrayOne[arrayOnePtr]
        arrayTwoEle = arrayTwo[arrayTwoPtr]
        currDiff = abs(arrayOneEle - arrayTwoEle)

        if currDiff < minDiff:
            minDiff = currDiff
            result = [arrayOneEle, arrayTwoEle]

            if minDiff == 0:
                return result

        if arrayOneEle < arrayTwoEle:
            arrayOnePtr += 1
        else:
            arrayTwoPtr += 1

    return result
