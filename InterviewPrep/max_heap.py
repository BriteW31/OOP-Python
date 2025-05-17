"""
MaxHeap Class
"""
from min_heap import MinHeap

class MaxHeap:
    def __init__(self):
        self.heap = MinHeap()
    
    def push(self, val):
        self.heap.push(-val)

    def pop(self):
        return -self.heap.pop()

    def top(self):
        if len(self.heap) > 0:
            return -self.heap.top() 
        else:
            return None

    def __len__(self):
        return len(self.heap)    