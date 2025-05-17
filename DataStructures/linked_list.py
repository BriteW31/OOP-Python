"""
Linked List Class
"""

from node import Node

class LinkedList(Node):
    def __init__(self, data):
        super().__init__(data)
        self.next: LinkedList = None
        self.prev: LinkedList = None
    
    def set_next_node(self, node: Node):
        self.next = node
    
    def set_prev_node(self, node: Node):
        self.prev = node