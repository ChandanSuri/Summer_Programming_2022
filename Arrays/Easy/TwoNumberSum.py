def TwoNumberSum(array, targetSum):
    distValues = set(array)

    for value in array:
        possibleSecValue = targetSum - value
        if value != possibleSecValue and possibleSecValue in distValues:
            return [possibleSecValue, value]

    return []
