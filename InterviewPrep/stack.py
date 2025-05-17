"""
Stack Class
"""

class Stack:
    def __init__(self):
        self.__stack = []
    
    def push(self, value):
        self.__stack.append(value)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.__stack.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.__stack[-1]
    
    def is_empty(self):
        return len(self.__stack) == 0
    
    def stack_size(self):
        return len(self.__stack)    