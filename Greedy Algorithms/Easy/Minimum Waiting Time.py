def minimumWaitingTime(queries):
    queries.sort()
    runningSum = finalSum = 0

    for idx in range(len(queries) - 1):
        runningSum += queries[idx]
        finalSum += runningSum

    return finalSum
