# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True

    if tree.value < minValue or tree.value >= maxValue:
        return False

    return validateBstHelper(tree.left, minValue, tree.value) and validateBstHelper(tree.right, tree.value, maxValue)

# SIMPLER SOLUTION
'''
def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True

    return minValue <= tree.value < maxValue and \
           validateBstHelper(tree.left, minValue, tree.value) and \
           validateBstHelper(tree.right, tree.value, maxValue)
'''
