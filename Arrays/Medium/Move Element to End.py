def moveElementToEnd(array, toMove):
    leftIdx = 0
    rightIdx = len(array) - 1

    while leftIdx < rightIdx:
        if array[rightIdx] == toMove:
            rightIdx -= 1
            continue
        elif array[leftIdx] == toMove:
            array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
            rightIdx -= 1

        leftIdx += 1

    return array
