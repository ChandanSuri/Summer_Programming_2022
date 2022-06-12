# O(N) time and O(1) space as In pLace!
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Iterative Solution
def removeDuplicatesFromLinkedList(linkedList):
    if linkedList is None:
        return linkedList

    currNode = linkedList
    while currNode.next is not None:
        if currNode.next.value == currNode.value:
            currNode.next = currNode.next.next
        else:
            currNode = currNode.next

    return linkedList


# Recursive Solution
def removeDuplicatesFromLinkedList(linkedList):
    head = linkedList
    removeDuplicatesFromLinkedListHelper(linkedList)
    return head

def removeDuplicatesFromLinkedListHelper(linkedList):
    if linkedList is None or linkedList.next is None:
        return linkedList

    if linkedList.next.value == linkedList.value:
        linkedList.next = linkedList.next.next
    else:
        linkedList = linkedList.next

    removeDuplicatesFromLinkedList(linkedList)

    return linkedList
