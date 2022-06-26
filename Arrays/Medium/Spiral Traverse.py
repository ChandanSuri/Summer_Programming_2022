def spiralTraverse(array):
    result = []
    startRow = startCol = 0
    endRow = len(array) - 1
    endCol = len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for idx in range(startCol, endCol + 1):
            result.append(array[startRow][idx])
        startRow += 1

        for idx in range(startRow, endRow + 1):
            result.append(array[idx][endCol])
        endCol -= 1

        if startRow <= endRow:
            for idx in range(endCol, startCol - 1, -1):
                result.append(array[endRow][idx])
            endRow -= 1

        if startCol <= endCol:
            for idx in range(endRow, startRow - 1, -1):
                result.append(array[idx][startCol])
            startCol += 1

    return result
