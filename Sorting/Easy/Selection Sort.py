def selectionSort(array):
    arrLen = len(array)

    for idx in range(arrLen):
        selIdx = idx
        # Finding the minimum and replacing it with the current index (ongoing lowest index)
        for jdx in range(idx + 1, arrLen):
            if array[jdx] < array[selIdx]:
                selIdx = jdx

        array[idx], array[selIdx] = array[selIdx], array[idx]

    return array
