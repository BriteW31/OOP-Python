"""
Median Stream class, using two different Heaps
"""

from min_heap import MinHeap
from max_heap import MaxHeap

class MedianStream:
    def __init__(self):
        self.low = MaxHeap()  
        self.high = MinHeap()  

    # insert_num inserts a value into the heap
    def insert_num(self, num):
        self.low.push(num)
        print(self.low.heap.data)
        self.high.push(self.low.pop())
        print(self.low.heap.data)
        print(self.high.data)
        if len(self.low) < len(self.high):
            print("True")
            self.low.push(self.high.pop())
            print(self.low.heap.data)
        print("-------")
    
    # calculates the median from heaps 
    def median(self):
        if len(self.low) > len(self.high):
            return self.low.top() / 1
        else:
            return (self.low.top() + self.high.top()) / 2
    


# median_stream returns the medians in the data stream
def median_stream(array):
    medians = MedianStream()
    median_array = []
    
    for num in array:
        medians.insert_num(num)
        median_array.append(medians.median())
        
    return median_array

# testing
array = [5, 15, 20, 3, 2, 8]
median_array = median_stream(array)
print(median_array)