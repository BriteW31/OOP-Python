"""
TreeSort Algorithm
"""

from node import Node
from binary_tree import BinaryTree as BTree

class TreeSort:
    def __init__(self):
        self.root = None

    def __insert(self, key):
        # define node to insert value into binary tree
        new_node = BTree(key)
        if self.root == None:
            self.root = new_node
        else:
            self.__insert_in_binary_tree(self.root, new_node)
    
    def __insert_in_binary_tree(self, tree_node, new_node):   
        # check if nodes in left and right branches exist
        if new_node.data <= tree_node.data:
            if tree_node.left == None:
                tree_node.left = new_node
            else:
                self.__insert_in_binary_tree(tree_node.left, new_node)
        else:
            if tree_node.right == None:
                tree_node.right = new_node
            else:
                self.__insert_in_binary_tree(tree_node.right, new_node)
    
    def append_binary_tree(self, node, array):
        # append all data into array in left-top-right direction
        if node != None:
            self.append_binary_tree(node.left, array)
            array.append(node.data)
            self.append_binary_tree(node.right, array)
    
    def traverse_binary_tree(self, node):
        if node != None:
            print(node.data)
            #print(node.left.data if node.left != None else "None")
            #print(node.right.data if node.right != None else "None")
            #print("*********")            
            #print(node.data, end = " ")
            self.traverse_binary_tree(node.left)
            self.traverse_binary_tree(node.right)       
            
    
    def sort(self, array):
        # insert all numbers in array into tree
        for number in array:
            self.__insert(number)

"""
# testing
array = [6, 2, 5, 11, 4, 6, -7, 2, 5]
sorted_array = TreeSort()
sorted_array.sort(array)
output_array = []
sorted_array.append_binary_tree(sorted_array.root, output_array)
print(output_array)
sorted_array.traverse_binary_tree(sorted_array.root)
"""