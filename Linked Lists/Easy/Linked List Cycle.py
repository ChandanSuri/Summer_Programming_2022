# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # This is a linear time and constant space solution.
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None:
            return False

        slow_ptr = head
        fast_ptr = head.next

        while fast_ptr != slow_ptr:
            if fast_ptr is None or fast_ptr.next is None:
                return False
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return True
