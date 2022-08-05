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

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if self is None or (self.left is None and self.right is None):
            return
        # check for left leaf
        if self.left.value == value and self.left.left is None and self.left.right is None:
            self.left = None
        # check for right leaf
        elif self.right.value == value and self.right.left is None and self.right.right is None:
            self.right = None
        # check for element to the left of root
        elif self.left.value == value:
            left_subtree = self.left.left
            self.left = self.left.right
            traversal_ptr = self.left
            while traversal_ptr.left is not None:
                traversal_ptr.left = traversal_ptr.left.left
            traversal_ptr.left = left_subtree
        # check for element to the right of root
        elif self.right.value == value:
            left_subtree = self.right.right
            self.right = self.right.left
            traversal_ptr = self.right
            while traversal_ptr.right is not None:
                traversal_ptr.right = traversal_ptr.right.right
            traversal_ptr.right = left_subtree

        return self.value
