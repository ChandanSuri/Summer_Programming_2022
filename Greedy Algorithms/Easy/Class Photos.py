# O(NlogN) time and O(1) space
def classPhotos(redShirtHeights, blueShirtHeights):
    backRow = sorted(blueShirtHeights)
    frontRow = sorted(redShirtHeights)

    if frontRow[0] > backRow[0]:
        tempArr = frontRow
        frontRow = backRow
        backRow = tempArr

    for idx in range(len(backRow)):
        if backRow[idx] <= frontRow[idx]:
            return False

    return True
