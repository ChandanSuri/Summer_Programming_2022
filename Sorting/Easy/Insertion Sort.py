def insertionSort(array):
    arrLen = len(array)

    for idx in range(1, arrLen):
        counterIdx = idx
        while counterIdx > 0 and array[counterIdx] < array[counterIdx - 1]:
            array[counterIdx], array[counterIdx - 1] = array[counterIdx - 1], array[counterIdx]
            counterIdx -= 1

    return array
