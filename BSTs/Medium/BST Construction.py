# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
                return
            self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
                return
            self.right.insert(value)

        return self

    def contains(self, value):
        if self is None:
            return False

        if value < self.value:
            return self.left.contains(value)
        elif value > self.value:
            return self.right.contains(value)
        else:
            return True

    def findNodeToRemove(self, parentNode, value):
        if self is None:
            return None, None

        if value < self.value:
            return self.left.findNodeToRemove(self, value)
        elif value > self.value:
            return self.right.findNodeToRemove(self, value)
        else:
            # Found the node
            return self, parentNode

    def getMaxElementFromLeftSubtree(self):
        prevNode = currNode = self.left

        while currNode.right is not None:
            prevNode = currNode
            currNode = currNode.right
        prevNode.right = None

        return currNode

    def remove(self, value):
        nodeToRemove, parentNode = self.findNodeToRemove(self, value)
        if nodeToRemove is None:
            return None

        if nodeToRemove.left is None and nodeToRemove.right is None:
            if parentNode.left == nodeToRemove:
                parentNode.left = None
            else:
                parentNode.right = None
        elif nodeToRemove.left is None or nodeToRemove.right is None:
            if parentNode.left == nodeToRemove:
                parentNode.left = nodeToRemove.left
            else:
                parentNode.right = nodeToRemove.right
        else:
            currNode = nodeToRemove.left.getMaxElementFromLeftSubtree()
            nodeToRemove.value = currNode.value

        return nodeToRemove
