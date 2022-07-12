# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # This solution is using the parent pointers
    # O(n) time and O(n) space solution.
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        parentNodesMap = {root: None}
        stack = [root]

        # We will try to get the parents of both the p and q nodes along with all it's ancestors.
        while p not in parentNodesMap or q not in parentNodesMap:
            currNode = stack.pop()

            if currNode.left is not None:
                parentNodesMap[currNode.left] = currNode
                stack.append(currNode.left)
            if currNode.right is not None:
                parentNodesMap[currNode.right] = currNode
                stack.append(currNode.right)

        # We will get all the ancestors of p till we go to the root Node
        ancestors = set()
        currNode = p
        while currNode is not None:
            ancestors.add(currNode)
            currNode = parentNodesMap[currNode]

        # We will iterate over all the ancestors of q node
        # till one of them matches with the ancestors of node p.
        while q not in ancestors:
            q = parentNodesMap[q]

        return q
