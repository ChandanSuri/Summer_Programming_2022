# Tip: You can use the type(element) to check whether an item is a list or an integer
# O(N) time and O(d) space where d is the maximum depth in the "special" arrays
def productSum(array):
    return productSumHelper(array, 1)


def productSumHelper(array, depth):
    currSum = 0
    for element in array:
        if type(element) is list:
            currSum += productSumHelper(element, depth + 1)
        else:
            currSum += element

    return currSum * depth
