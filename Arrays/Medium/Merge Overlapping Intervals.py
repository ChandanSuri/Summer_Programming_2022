def mergeOverlappingIntervals(intervals):
    intervals = sorted(intervals, key=lambda ele: ele[0])
    currInterval = intervals[0]
    mergedIntervals = list()

    for idx in range(1, len(intervals)):
        nextInterval = intervals[idx]

        if currInterval[1] >= nextInterval[0]:
            currInterval[1] = max(currInterval[1], nextInterval[1])
        else:
            mergedIntervals.append(currInterval)
            currInterval = nextInterval

    mergedIntervals.append(currInterval)

    return mergedIntervals
