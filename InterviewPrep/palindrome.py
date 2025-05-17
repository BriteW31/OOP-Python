"""
Palindrome Solution
"""

class Palindrome:
    def __init__(self, string):
        self.string = string

    # expand_center expands the middle of a string to include all consecutive duplicate characters
    def __expand_center(self, left, right):
        while left >= 0 and right < len(self.string) and self.string[left] == self.string[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    def longest_palindrome(self):
        # if not string, return nothing
        if not self.string:
            return ""
    
        # initialize start, end index
        start = 0
        end = 0
        
        # for every character, set it as middle, and find expand where necessary
        for index in range(len(self.string)):
            len1 = self.__expand_center(index, index)     
            len2 = self.__expand_center(index, index + 1) 
            max_len = max(len1, len2)
    
            # sets up palindrome
            if max_len > end - start:
                start = index - (max_len - 1) // 2
                end = index + max_len // 2
    
        return self.string[start:end + 1]
    


test_s = "babcad"
test_s2 = "cbabcbabc"

palindrome = Palindrome(test_s)
palindrome2 = Palindrome(test_s2)

# Output: "bab"
longest = palindrome.longest_palindrome()
print(longest)  

# Output: 'cbabcbabc'
longest2 = palindrome2.longest_palindrome()
print(longest2)

