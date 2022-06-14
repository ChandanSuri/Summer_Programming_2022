def bubbleSort(array):
    for idx in range(len(array) - 1):
        isSorted = True
        for jdx in range(len(array) - idx - 1):
            if array[jdx] > array[jdx + 1]:
                array[jdx], array[jdx + 1] = array[jdx + 1], array[jdx]
                isSorted = False

        if isSorted:
            break

    return array

