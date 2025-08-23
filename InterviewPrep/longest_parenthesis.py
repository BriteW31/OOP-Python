"""
Longest Valid Parenthesis Expression
"""

def longestParentheses(s):
    # initialize variables
    left = 0
    right = 0
    max_length = 0
    
    # left to right to get first possible maximum length
    for i in range(0, len(s)):
        if s[i] == "(":
            left += 1
        else:
            right += 1
        
        if left == right:
            max_length = max(max_length, 2 * right)
        elif right > left:
            left = 0
            right = 0
    
    # initialize variables
    left = 0
    right = 0
    
    # right to left to possibly get a new maximum length
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ")":
            right += 1
        else:
            left += 1
        
        if left == right:
            max_length = max(max_length, 2 * left)
        elif left > right:
            left = 0
            right = 0        
    
    return max_length

# alternate method uses stack
def longestParenthesisAlt(s):
    stack = [-1]
    max_length = 0
    
    for i, ch in enumerate(s):
        if ch == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    
    return max_length

def maxPairs(s):
    max_length = longestParenthesisAlt(s)
    max_pairs = max_length // 2
    return max_pairs

# test
s = "(()()()))()()()()()"
print(longestParentheses(s)) 
print(longestParenthesisAlt(s)) 
print(maxPairs(s))