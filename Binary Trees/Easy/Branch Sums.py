"""
For this problem:
1. When you need to do some operation like where you have to go to the
complete depth of the tree again and again, consider the DFS solution in
trees or graphs for doing so.
2. Mutate your DFS solution in order to serve your purpose. The traversals
like inorder, preorder and postorder are sometimes helpful in doing so!
3. When using recursion for problems like these, consider your base cases
first and see when you want to return the data and when you want to return
nothing (if that's the case). Checking for None's at the correct point in
code is an important part of the solution.
"""


# O(N) time and O(N) space
def branchSums(root):
    branchSumsArr = []
    branchSumsHelper(root, branchSumsArr, 0)
    return branchSumsArr


def branchSumsHelper(node, branchSumsArr, currentRunningSum):
    if node is None:
        return

    currentRunningSum += node.value
    if node.left is None and node.right is None:
        branchSumsArr.append(currentRunningSum)

    branchSumsHelper(node.left, branchSumsArr, currentRunningSum)
    branchSumsHelper(node.right, branchSumsArr, currentRunningSum)


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
