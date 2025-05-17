"""
Operations Class
"""

from stack import Stack
from error_operations import ErrorOperations

class Operations:
    def __init__(self, string):
        self.string = string

    # Tokenize splits string into smaller parts
    def __tokenize(self):
        # initialize array to hold characters, index tracker
        tokens = []
        index = 0
        
        # begin count
        while index < len(self.string):
            # if space, increase index by 1
            if self.string[index].isspace():
                index += 1
                
            # if the char is a +, (, or )
            elif self.string[index] in '+()':
                tokens.append(self.string[index])
                index += 1                
                
            # if char is -, it can mean it is a -, or a negative number
            elif self.string[index] == '-':
                if index == 0 or self.string[index] in ' (+-':
                    temp_index = index + 1
                    while temp_index < len(self.string) and self.string[temp_index].isdigit():
                        temp_index += 1
                    tokens.append(self.string[index:temp_index])
                    index = temp_index      
                else:
                    tokens.append(self.string[index])
       
            # if it is a digit
            elif self.string[index].isdigit():
                # initialize temp_index to track numbers
                
                temp_index = index
                # appends all digits until next char is not a digit
                while temp_index < len(self.string) and self.string[temp_index].isdigit():
                    temp_index += 1
                tokens.append(self.string[index:temp_index])
                # increases index by value of temp_index
                index = temp_index
                
            else:
                # error
                return -1
            
        # return array
        return tokens
    
    # precedence determines if symbol (which is a char) is +, or -
    def __precedence(self, symbol):
        # returns 2 if symbol is "u-"
        if symbol == '*':
            return 2
        # returns 1 if the symbol is "+", "-"
        if symbol in ('+', '-'):
            return 1
        # returns 0 otherwise
        return 0
    
    # to_postfix converts a token array into postfix notation
    # example: ["2", "+", "3", "-", "5"] => ["2", "3", "5", "-", "+"]
    def __to_postfix(self, tokens):
        # initialize output, stack
        output = []
        stack = Stack()
        
        # appends all tokens
        for token in tokens:
            # if number, appends to token
            if token.lstrip('-').isdigit():
                output.append(token)
                
            # if + or -, then check if ( and ) exist, and append token to stack, and all numbers to output
            elif token in '+-':
                while not stack.is_empty() and stack.peek() != '(' and self.__precedence(stack.peek()) >= self.__precedence(token):
                    output.append(stack.pop())
                stack.push(token)
                
            # if (, then append to stack
            elif token == '(':
                stack.push(token)
                
            # if ), append everything in stack from ( to output
            elif token == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    output.append(stack.pop())
                stack.pop()
                    
        while not stack.is_empty():
            # appends everything else to output
            output.append(stack.pop())
            
        # return output
        return output
    
    # eval_postfix evaluates the postfix array
    def __eval_postfix(self, postfix):
        # initialize stack
        stack = Stack()
        
        # appends all digits to stack
        for token in postfix:
            if token.lstrip('-').isdigit():
                stack.push(int(token))
            
            # if token is + or -, appends the sum or difference by popping previous two elements
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.push(a + b)
                elif token == '-':
                    stack.push(a - b)
                elif token == '*':
                    stack.push(a * b)
                
        # returns stack's first value
        return stack.pop()
    
    # operations returns the final result of the expression
    def operations(self):
        token_array = self.__tokenize()
        
        # error
        if token_array == -1:
            return "Invalid Symbols in Expression"
        
        print(token_array)
        
        # if valid token_array, check for correct syntax
        error_check = ErrorOperations(token_array)
        error_bool = error_check.error_operations()
        if error_bool:
            return "Invalid Expression"
        else:
            postfix_array = self.__to_postfix(token_array)
            print(postfix_array)
            
            return self.__eval_postfix(postfix_array)


# Test example
expression = "1- ((1) + 2 - (0- 20 -    18) + (1 + (   -2)) -(6- (3    -    (1+1)   ) ))  "
expression_2 = "  100 + ((-1) + 2 - (-20 -    -18) + (1 + (   -2))) -(   6- (3    -    (-1+1))) "
expression_3 = "    (1) + 2 - (0- 20 -    18) + (1 + (   -2)) -(6- (3    -    (1+1)   ) )  "
expression_4 = " 100 +((-1) + 2 - (-20 -    (-18)) + (1 + (   -2))) -(   6- (3    -    (-1+1)))   "
expression_5 = " ((-1) +   + 2 - (-20 -    -18) + (1 + (   -2))) -(   6- (3    -    (-1+1)))   "
expression_6 = " ((-1)   + 2 - (-20 -    (-18)) ^ (1 + (   -2))) +(   6- (3    -    (-1+1)))   "
expression_7 = "1 + (-3)"
expression_8 = "1- (-1 + 2 - (0- 20 -    18) + (1 + (1   - 2)) -(6- (3    -    (1+1)   ) ))  "

operation = Operations(expression)
operation_2 = Operations(expression_2)
operation_3 = Operations(expression_3)
operation_4 = Operations(expression_4)
operation_5 = Operations(expression_5)
operation_6 = Operations(expression_6)
operation_7 = Operations(expression_7)
operation_8 = Operations(expression_8)

# Output: -34
print("Expression 1: " + "\n" + expression)
print("Result: " + "\n" + str(operation.operations()))

# Output: Invalid Expression
print("\nExpression 2: " + "\n" + expression_2)
print("Result: " + "\n" + str(operation_2.operations()))

# Output: 35
print("\nExpression 3: " + "\n" + expression_3)
print("Result: " + "\n" + str(operation_3.operations()))

# Output: 99
print("\nExpression 4: " + "\n" + expression_4)
print("Result: " + "\n" + str(operation_4.operations()))

# Output: "Invalid Expression"
print("\nExpression 5: " + "\n" + expression_5)
print("Result: " + "\n" + str(operation_5.operations()))

# Output: "Invalid Symbols in Expression"
print("\nExpression 6: " + "\n" + expression_6)
print("Result: " + "\n" + str(operation_6.operations()))

# Output: -2
print("\nExpression 7: " + "\n" + expression_7)
print("Result: " + "\n" + str(operation_7.operations()))

# Output: -33
print("\nExpression 8: " + "\n" + expression_8)
print("Result: " + "\n" + str(operation_8.operations()))