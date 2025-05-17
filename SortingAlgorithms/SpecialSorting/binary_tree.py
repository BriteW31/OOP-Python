"""
Binary Search Tree Class
"""

from node import Node

class BinaryTree(Node):
    def __init__(self, data):
        super().__init__(data)
        self.left: BinaryTree = None
        self.right: BinaryTree = None
    
    def set_left_tree(self, node: Node):
        self.left = node
    
    def set_right_tree(self, node: Node):
        self.right = node