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
        # Write your code here.
        # Do not edit the return statement of this method.
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
        # Write your code here.
        if self is None:
            return False

        if value < self.value:
            return self.left.contains(value)
        elif value > self.value:
            return self.right.contains(value)
        else:
            return True

    def findNodeToRemove(self, value):
        if self is None:
            return None

        if value < self.value:
            return self.left.findNodeToRemove(value)
        elif value > self.value:
            return self.right.findNodeToRemove(value)
        else:
            # Found the node
            return self

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        nodeToRemove = self.findNodeToRemove(value)
        if nodeToRemove is None:
            return None

        if nodeToRemove.right is None and nodeToRemove.right is None:
            # Node to be removed has no children
            pass
        elif nodeToRemove.right is None:
            nodeToRemove.value = nodeToRemove.left.value
        else:
            pass

        return self
