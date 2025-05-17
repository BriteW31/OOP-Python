"""
Circular Linked List
"""
# import class
from NodeClass import LinkedListNode as Node

def Circular(head):
    # trivial case
    if not head:
        return False
    
    # track nodes with tracker variable as target
    tracker = head
    
    # loop through linked list so long as either head is not null,
    # or head.next is not the target
    while head and head.next != tracker:
        head = head.next
    
    # linked list ends without loop, not circular
    if not head or not head.next:
        return False
    
    # otherwise, circular
    return True


# testing - true
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head

if Circular(head):
    print("True")
else:
    print("False")

# this is different from first, gives false
head_1 = Node(1)
head_1.next = Node(2)
head_1.next.next = Node(3)
head_1.next.next.next = Node(4)
head_1.next.next.next.next = Node(5)
head_1.next.next.next.next.next = Node(6)
head_1.next.next.next.next.next.next = Node(1)

if Circular(head_1):
    print("True")
else:
    print("False")

# testing - not circular
head_2 = Node(1)
head_2.next = Node(2)
head_2.next.next = Node(3)
head_2.next.next.next = Node(4)
head_2.next.next.next.next = Node(5)
head_2.next.next.next.next.next = Node(6)

if Circular(head_2):
    print("True")
else:
    print("False")

"""
# testing - never terminates case, dead loop
head_3 = Node(1)
head_3.next = Node(2)
head_3.next.next = Node(3)
head_3.next.next.next = Node(4)
head_3.next.next.next.next = Node(5)
head_3.next.next.next.next.next = Node(6)
head_3.next.next.next.next.next.next = head_3.next

if Circular(head_3):
    print("True")
else:
    print("False")
"""