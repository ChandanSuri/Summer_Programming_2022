# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # This solution has O(N) time complexity and O(D) space complexity
    # where N is the number of nodes and D is the maximum diameter of the tree.
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        nextLevelQueue = list()
        nextLevelQueue.append(root)
        rightSideView = list()

        while len(nextLevelQueue) != 0:
            currLevelQueue = nextLevelQueue
            nextLevelQueue = list()
            for currNode in currLevelQueue:
                if currNode.left:
                    nextLevelQueue.append(currNode.left)
                if currNode.right:
                    nextLevelQueue.append(currNode.right)
            rightSideView.append(currNode.val)

        return rightSideView
