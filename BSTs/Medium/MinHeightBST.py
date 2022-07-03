# O(N) time and O(N) space solution
def minHeightBst(array):
    root = minHeightBstHelper(array, 0, len(array) - 1)
    return root


def minHeightBstHelper(array, startIdx, endIdx):
    if startIdx > endIdx:
        # For Leaf Nodes
        return None

    midIdx = startIdx + (endIdx - startIdx) // 2
    currValue = array[midIdx]

    currNode = BST(currValue)
    currNode.left = minHeightBstHelper(array, startIdx, midIdx - 1)
    currNode.right = minHeightBstHelper(array, midIdx + 1, endIdx)

    return currNode


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
