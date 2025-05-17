"""
Loop in a linked list
"""
# import class
from NodeClass import LinkedListNode

def LoopInLinkedList(head):
    # double pointers
    slow = head
    fast = head
    
    # while loop to track position
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # equal implies loop in linked list
        if slow == fast:
            return True
    
    return False

# testing - true
head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)
head.next.next.next.next = LinkedListNode(5)
head.next.next.next.next.next = LinkedListNode(6)
head.next.next.next.next.next.next = head.next.next

if LoopInLinkedList(head):
    print("True")
else:
    print("False")

# this is different from first, gives false
head_1 = LinkedListNode(1)
head_1.next = LinkedListNode(2)
head_1.next.next = LinkedListNode(3)
head_1.next.next.next = LinkedListNode(4)
head_1.next.next.next.next = LinkedListNode(5)
head_1.next.next.next.next.next = LinkedListNode(6)
head_1.next.next.next.next.next.next = LinkedListNode(3)

if LoopInLinkedList(head_1):
    print("True")
else:
    print("False")