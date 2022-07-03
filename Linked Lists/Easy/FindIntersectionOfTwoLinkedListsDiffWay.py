# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptrA = headA
        ptrB = headB

        lenA = self.findLenOfLinkedList(ptrA)
        lenB = self.findLenOfLinkedList(ptrB)
        diffInLens = lenA - lenB

        ptrA = headA
        ptrB = headB
        if diffInLens < 0:
            ptrB = self.traverseLinkedList(ptrB, abs(diffInLens))
        else:
            ptrA = self.traverseLinkedList(ptrA, abs(diffInLens))

        while ptrA and ptrB and ptrA != ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next

        return ptrA

    def findLenOfLinkedList(self, currNode):
        lenLinkedList = 0
        while currNode:
            lenLinkedList += 1
            currNode = currNode.next

        return lenLinkedList

    def traverseLinkedList(self, currNode, counter):
        while counter > 0:
            currNode = currNode.next
            counter -= 1

        return currNode
