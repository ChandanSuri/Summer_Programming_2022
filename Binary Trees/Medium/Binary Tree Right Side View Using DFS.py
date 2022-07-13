# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # This solution has O(N) time complexity and O(D) space complexity
    # where N is the number of nodes and D is the maximum depth of the tree.
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        heightNodeMap = dict()
        self.generateSideView(heightNodeMap, 0, root)
        return heightNodeMap.values()

    def generateSideView(self, heightNodeMap, currHeight, currNode):
        if currNode is None:
            return

        if currHeight not in heightNodeMap:
            heightNodeMap[currHeight] = currNode.val

        self.generateSideView(heightNodeMap, currHeight + 1, currNode.right)
        self.generateSideView(heightNodeMap, currHeight + 1, currNode.left)
