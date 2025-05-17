"""
Queue Class
"""

class Queue:
    def __init__(self):
        self.__queue: list = []
    
    def enqueue(self, element):
        self.__queue.append(element)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.__queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.__queue[0]
    
    def is_empty(self):
        return len(self.__queue) == 0
    
    def size(self):
        return len(self.__queue)