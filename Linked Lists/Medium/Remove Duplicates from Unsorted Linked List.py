# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # This is a O (n) solution with O(n) space complexity
        nums_count_map = dict()

        # Generating map of number of counts of each element
        curr_ptr = head
        while curr_ptr is not None:
            curr_value = curr_ptr.val
            nums_count_map[curr_value] = nums_count_map.get(curr_value, 0) + 1
            curr_ptr = curr_ptr.next

        # Deleting duplicates according to the count in the map
        curr_ptr = prev_ptr = head
        while curr_ptr is not None:
            curr_value = curr_ptr.val
            if nums_count_map[curr_value] > 1:
                if curr_ptr == head:
                    head = head.next
                    prev_ptr = curr_ptr = head
                else:
                    prev_ptr.next = curr_ptr.next
                    curr_ptr = curr_ptr.next
            else:
                prev_ptr = curr_ptr
                curr_ptr = curr_ptr.next

        return head
