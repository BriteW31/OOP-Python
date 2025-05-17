"""
MinHeap Class
"""

class MinHeap:
    def __init__(self):
        self.data = []
    
    # push appends, then moves the value up
    def push(self, val):
        self.data.append(val)
        self.__heapify_up(len(self.data) - 1)

    # pop removes the element at an index
    def pop(self):
        if not self.data:
            return None
        # swaps, then returns the value
        self.__swap(0, len(self.data) - 1)
        val = self.data.pop()
        self.__heapify_down(0)
        return val
    
    # returns the first value
    def top(self):
        if self.data:
            return self.data[0]
        else:
            return None
    
    # returns length of heap
    def __len__(self):
        return len(self.data)

    def __heapify_up(self, index):
        # find parent node
        parent = (index - 1) // 2
        # swaps the index with parent, then recursive call until the index reaches parent
        if parent >= 0 and self.data[index] < self.data[parent]:
            self.__swap(index, parent)
            self.__heapify_up(parent)

    def __heapify_down(self, index):
        # find child nodes, initialize temp for smallest
        child1 = 2 * index + 1
        child2 = 2 * index + 2
        smallest = index
        # if either child is smaller than temp, then replace
        if child1 < len(self.data) and self.data[child1] < self.data[smallest]:
            smallest = child1
        if child2 < len(self.data) and self.data[child2] < self.data[smallest]:
            smallest = child2
        # swaps index with smallest, then recursive call
        if smallest != index:
            self.__swap(index, smallest)
            self.__heapify_down(smallest)

    # swap swaps the values
    def __swap(self, i, j):
        # swap values
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp        
