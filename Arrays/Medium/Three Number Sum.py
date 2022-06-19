def threeNumberSum(array, targetSum):
    """
    Sorting the array is required as the triplets should be sorted as well
    as the elements inside the triplets needs to be sorted. Sorting the
    full array beforehand will be computationally less expensive than
    sorting the triplets at a later point in time.
    """
    array.sort()
    arrLen = len(array)
    triplets = list()

    for idx in range(arrLen - 2):
        remainingSum = targetSum - array[idx]
        leftIdx = idx + 1
        rightIdx = arrLen - 1

        while leftIdx < rightIdx:
            currentSum = array[leftIdx] + array[rightIdx]

            if currentSum == remainingSum:
                triplets.append([array[idx], array[leftIdx], array[rightIdx]])
                leftIdx += 1
                rightIdx -= 1
            elif currentSum < remainingSum:
                leftIdx += 1
            else:
                rightIdx -= 1

    return triplets
