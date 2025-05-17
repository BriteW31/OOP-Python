"""
Remove loop in LinkedList
"""
# import class
from NodeClass import LinkedListNode as Node

def RemoveLoop(head):
    # trivial cases
    if head is None:
        return
    if head.next is None:
        return
    
    # define two pointers
    slow = head
    fast = head
    
    # rotate until either termination, or a loop is detected
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # loop detected
        if slow == fast:
            slow = head
            
            # traverse until node is found
            while slow != fast:
                slow = slow.next
                fast = fast.next
                
            # find the next node
            while fast.next != slow:
                fast = fast.next
                
            # remove node that creates the loop
            fast.next = None

# Printer prints the final product
def Printer(current):
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("End")


# testing - Circular Linked List
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head

RemoveLoop(head)
Printer(head)

# loop in Linked List
head_1 = Node(1)
head_1.next = Node(2)
head_1.next.next = Node(3)
head_1.next.next.next = Node(5)
head_1.next.next.next.next = Node(8)
head_1.next.next.next.next.next = Node(13)
head_1.next.next.next.next.next.next = head_1.next.next

RemoveLoop(head_1)
Printer(head_1)