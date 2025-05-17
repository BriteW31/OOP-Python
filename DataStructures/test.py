"""
Test File
"""

from binary_tree import BinaryTree
from linked_list import LinkedList
from stack import Stack
from queue import Queue



def create_linked_list():
    root = LinkedList(6)
    root.next = LinkedList(5)
    root.next.next = LinkedList(9)
    root.next.prev = root
    print(root.data)
    print(root.next.data)
    print(root.next.prev.data)
    if root.prev == None:
        print("empty")
    
    temp = root.next.next
    temp.next = LinkedList(10)
    temp.next.next = LinkedList(4)
    print(temp.next.next.data)    

def create_binary_tree():
    root = BinaryTree(6)
    root.left = BinaryTree(5)
    root.right = BinaryTree(9)
    print(root.data)
    print(root.left.data)
    print(root.right.data)

    temp = root.left
    temp.left = BinaryTree(10)
    temp.right = BinaryTree(4)
    print(root.left.left.data)

create_linked_list()
print("\n")
create_binary_tree()
