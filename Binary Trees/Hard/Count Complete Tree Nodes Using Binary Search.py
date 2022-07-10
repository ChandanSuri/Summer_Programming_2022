# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        depth = self.getDepth(root)
        if depth == 0:
            return 1

        numNodes = 2 ** depth - 1

        leftIdx = 0
        rightIdx = 2 ** depth - 1

        while leftIdx <= rightIdx:
            midIdx = leftIdx + (rightIdx - leftIdx) // 2
            if self.exists(midIdx, depth, root):
                leftIdx = midIdx + 1
            else:
                rightIdx = midIdx - 1

        numNodes += leftIdx

        return numNodes

    def getDepth(self, node):
        depth = 0

        while node.left is not None:
            node = node.left
            depth += 1

        return depth

    def exists(self, currIdx, depth, node):
        leftIdx = 0
        rightIdx = 2 ** depth - 1

        for idx in range(depth):
            midIdx = leftIdx + (rightIdx - leftIdx) // 2
            if currIdx <= midIdx:
                node = node.left
                rightIdx = midIdx
            else:
                node = node.right
                leftIdx = midIdx + 1

        return node is not None
