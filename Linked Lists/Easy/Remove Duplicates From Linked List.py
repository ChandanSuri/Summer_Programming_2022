# O(N) time and O(1) space as In pLace!
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Iterative Solution
def removeDuplicatesFromLinkedList(linkedList):
    currNode = linkedList
    while currNode.next is not None:
        if currNode.next.value == currNode.value:
            currNode.next = currNode.next.next
        currNode = currNode.next

    return linkedList


# Recursive Solution
def removeDuplicatesFromLinkedList(linkedList):
    if linkedList.next is None:
        return

    if linkedList.next.value == linkedList.value:
        linkedList.next = linkedList.next.next

    removeDuplicatesFromLinkedList(linkedList.next)

    return linkedList
