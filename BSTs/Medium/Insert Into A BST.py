# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if root is None:
            root = TreeNode(val)
            return root

        if val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
                return root
            self.insertIntoBST(root.left, val)
        else:
            if root.right is None:
                root.right = TreeNode(val)
                return root
            self.insertIntoBST(root.right, val)

        return root
