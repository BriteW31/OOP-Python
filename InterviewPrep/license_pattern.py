"""
nth License Pattern of 5; order is numbers first, then letters
"""

class LicensePattern:
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def __writeNumbers(self, num, req_length):
        return num.zfill(req_length)

    def getPattern(self, n):
        # since n starts at 1, with string starting as 00000, the index is actually n - 1
        index = n - 1
        positions = 5  # license plates of length 5 max
    
        # determine how many letters at the end
        num_digits = 5
        total = 10 ** 5
        letters = 0
        
        # determines number of numbers, letters required in the license plate
        while index >= total:
            index -= total
            letters += 1
            num_digits = 5 - letters
            total = (10 ** num_digits) * (26 ** letters)
    
        # split numeric and letters
        number_part = index % (10 ** num_digits)
        char_part = index // (10 ** num_digits)

        # only write number part if there is space for numbers
        if num_digits > 0:
            first_part = self.__writeNumbers(str(number_part), num_digits)
        else:
            # otherwise, do nothing
            first_part = ""
    
        # write letter part
        second_part = ""
        leftover_letters = letters
        
        # leftover space will be used to write down the letters needed
        while leftover_letters > 0:
            second_part = self.letters[char_part % 26] + second_part
            char_part //= 26
            leftover_letters -= 1
    
        # return final result
        return first_part + second_part
    

# testing
sol = LicensePattern()

print(sol.getPattern(1))        # 00000, which is the minimum before out of range
print(sol.getPattern(3))        # 00002
print(sol.getPattern(100000))   # 99999
print(sol.getPattern(100001))   # 0000A
print(sol.getPattern(110000))   # 9999A
print(sol.getPattern(110001))   # 0000B
print(sol.getPattern(120001))   # 0000C
print(sol.getPattern(360000))   # 9999Z
print(sol.getPattern(360001))   # 000AA

# random tests
print(sol.getPattern(12345))    # 12344
print(sol.getPattern(234567))   # 4566N
print(sol.getPattern(5234687))  # 6NXCU
print(sol.getPattern(7363360))  # 9ZZZZ
print(sol.getPattern(7363361))  # AAAAA
print(sol.getPattern(19244736)) # ZZZZZ, which is the maximum before out of range

