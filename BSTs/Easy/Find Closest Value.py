def findClosestValueInBstHelper(node, target, runningClosest):
    if node is None:
        return runningClosest

    if abs(node.value - target) < abs(runningClosest - target):
        runningClosest = node.value

    if target == node.value:
        return node.value
    elif target >= node.value:
        return findClosestValueInBstHelper(node.right, target, runningClosest)
    else:
        return findClosestValueInBstHelper(node.left, target, runningClosest)


def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None