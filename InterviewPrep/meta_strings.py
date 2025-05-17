"""
Meta Strings
"""

class MetaStrings: 
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
    
    def __swap(self, str_list, i, j):
        temp = str_list[i]
        str_list[i] = str_list[j]
        str_list[j] = temp
    
    def meta_strings(self):
        # if different lengths, or equal strings
        if len(self.str1) != len(self.str2) or self.str1 == self.str2:
            return False
    
        # track where the characters are different
        first = -1
    
        for i in range(len(self.str1)):
            # if characters not equal, send track
            if self.str1[i] != self.str2[i]:
                if first == -1:
                    first = i
                # if track is not -1, then begin swap
                else:
                    # initialize list of the string, then swap
                    str1_list = list(self.str1)
                    self.__swap(str1_list, first, i)
                    
                    # join the list to form str1 with the swap
                    new_str1 = "".join(str1_list)
                    
                    # if equal, then true
                    if new_str1 == self.str2:
                        return True
                    else:
                        return False
        
        # otherwise, false
        return False

# testing
meta_strings = MetaStrings("converse", "conserve")
print(meta_strings.meta_strings())

meta_strings2 = MetaStrings("apple", "apple")
print(meta_strings2.meta_strings())

meta_strings3 = MetaStrings("abcde", "abcef")
print(meta_strings3.meta_strings())


