# This had to be done without sorting, O(N) time and O(1) space as just 3 integers array
def findThreeLargestNumbers(array):
    threeLargestNums = [float("-inf"), float("-inf"), float("-inf")]

    for element in array:
        if element > threeLargestNums[2]:
            threeLargestNums[0] = threeLargestNums[1]
            threeLargestNums[1] = threeLargestNums[2]
            threeLargestNums[2] = element
        elif element > threeLargestNums[1]:
            threeLargestNums[0] = threeLargestNums[1]
            threeLargestNums[1] = element
        elif element > threeLargestNums[0]:
            threeLargestNums[0] = element

    return threeLargestNums
