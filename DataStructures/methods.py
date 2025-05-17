"""
Methods Class
"""

class Methods:
    # Traverse preorder
    def traverse_pre_order(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traverse_pre_order()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder
    def traverse_in_order(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder
    def traverse_post_order(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')
    
    # Determine if binary tree is binary search tree
    def is_binary_search_tree(self, min_value, max_value):
        if self is None:
            return True
        if node.value > max_value or min_value > node.value:
            return False
        return is_binary_search_tree(self.left, min_value, node.value - 1) and is_binary_search_tree(self.right, node.value + 1, max_value)
    # Call is_binary_search_tree
    def is_binary_search(self):
        return is_binary_search_tree(self, float('-inf'), float('inf'))
    
    # Binary search to find a value
    def binary_search_tree_find_value(self, value):
        if is_binary_search_tree(self):
            if self is None or self.val == value:
                return self
            
            if value < self.val:
                return binary_search_tree_find_value(self.left, value)
            
            return binary_search_tree_find_value(self.right, value)
    
    # Method to add a node at the beginning of the LL
    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Method to add a node at any index
    # Indexing starts from 0.
    def insert_at_index(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return

        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")
    
    # Method to add a node at the end of LL
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
    
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
    
        current_node.next = new_node
    
    # Update node at a given position
    def update_node(self, val, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            current_node.data = val
        else:
            print("Index not present")
    
    # Method to remove first node of linked list
    def remove_first_node(self):
        if self.head is None:
            return
    
        self.head = self.head.next
    
    # Method to remove last node of linked list
    def remove_last_node(self):
        if self.head is None:
            return
    
        # If there's only one node
        if self.head.next is None:
            self.head = None
            return
    
        # Traverse to the second last node
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next
    
        current_node.next = None
    
    # Method to remove a node at a given index
    def remove_at_index(self, index):
        if self.head is None:
            return

        if index == 0:
            self.remove_first_node()
            return

        current_node = self.head
        position = 0
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")
    
    # Method to remove a node from the linked list by its data
    def remove_node(self, data):
        current_node = self.head
    
        # If the node to be removed is the head node
        if current_node is not None and current_node.data == data:
            self.remove_first_node()
            return
    
        # Traverse and find the node with the matching data
        while current_node is not None and current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
    
        # If the data was not found
        print("Node with the given data not found")
    
    # Print the size of the linked list
    def size_of_linked_list(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size
    
    # Print the linked list
    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next    