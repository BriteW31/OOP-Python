"""
Detect First Node in Loop of Linked List
"""

from NodeClass import LinkedListNode as Node

def first_node_loop(head):
    # initialize pointers
    slow = head
    fast = head
    
    # traverse through linked list with while loop
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # if loop found in linked list
        if slow == fast:
            slow = head
            # traverse until fast and slow meet, first node that creates loop
            while slow != fast:
                slow = slow.next
                fast = fast.next
            # returns node
            return slow
    # if no loop found
    return None

# loop in Linked List
head_1 = Node(1)
head_1.next = Node(2)
head_1.next.next = Node(3)
head_1.next.next.next = Node(5)
head_1.next.next.next.next = Node(8)
head_1.next.next.next.next.next = Node(13)
head_1.next.next.next.next.next.next = head_1.next.next

first_node = first_node_loop(head_1)
print(first_node.data)