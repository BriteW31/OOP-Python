"""
Stack Class
"""

class Stack:
    def __init__(self):
        self.__stack: list = []
    
    def push(self, value):
        self.__stack.append(value)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.__stack.pop(len(self.__stack) - 1)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.__stack[len(self.__stack) - 1]
    
    def is_empty(self):
        return len(self.__stack) == 0
    
    def stack_size(self):
        return len(self.__stack)