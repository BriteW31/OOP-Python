
class SumPairs:
    def __init__(self, array):
        self.array = array
    
    def sum_pairs(self, target):
        # define variables
        value_to_index = {}
        used_value_pairs = set()
        result = []
        
        for i, num in enumerate(self.array):
            # define complement as value needed between num and target
            complement = target - num
            # create tuple
            value_pair = tuple(sorted((num, complement)))
            
            # only record the first appearance of num
            if num not in value_to_index:
                value_to_index[num] = i            
            
            # check if the complement is already seen and unused
            if complement in value_to_index:
                # define temp variable for index from complement
                j = value_to_index[complement]  
                # if pairs are not used, append to result
                if value_pair not in used_value_pairs:
                    result.append((j, i))
                    # add to used pairs set
                    used_value_pairs.add(value_pair)
                    # "invalidate" both numbers
                    value_to_index.pop(complement)
                    # remove current num
                    value_to_index.pop(num, None)
                    # move to next number
                    continue

        # return final result
        return result       
    
    def sum_pairs_2(self, target):
        # define variables
        value_to_index = {}
        used_value_pairs = set()
        
        for i, num in enumerate(self.array):
            # Only record the first appearance of num
            value_to_index[num] = i
        
        print(value_to_index)
        
        for i, num in enumerate(self.array):
            # define complement as value needed between num and target
            complement = target - num
            # Check if the complement is already seen and unused
            if complement in value_to_index:
                j = value_to_index[complement]
                #if value_pair not in used_value_pairs:
                if (i < j):
                    used_value_pairs.add((i, j))
                else:
                    used_value_pairs.add((j, i))
      
        # Return final result
        return used_value_pairs

# testing
"""
array = [1, 5, 4, 5, 6, 3, -2, 9, 11, -1, 4, 0, 8, 1]
target = 9
pairs = SumPairs(array)
output = pairs.sum_pairs(target)
print(output)
"""
array_2 = [0, 1, 2, 5, 4, 2, 7, -2, 3, 4, 5, 3, 5, 1, 3, 5]
target_2 = 6
pairs_2 = SumPairs(array_2)
output_2 = pairs_2.sum_pairs(target_2)
print(output_2)

"""
    def sum_pairs_2(self, target):
        # define variables
        value_to_index = {}
        used_value_pairs = set()
        result = []
        
        for i, num in enumerate(self.array):
            # define complement as value needed between num and target
            complement = target - num
            # create tuple
            value_pair = tuple(sorted((num, complement)))
            
            # only record the first appearance of num
            if num not in value_to_index:
                value_to_index[num] = i            
            
            # check if the complement is already seen and unused
            if complement in value_to_index:
                # define temp variable for index from complement
                j = value_to_index[complement]  
                # if pairs are not used, append to result
                if value_pair not in used_value_pairs:
                    result.append((j, i))
                    # add to used pairs set
                    used_value_pairs.add(value_pair)
                    # "invalidate" both numbers
                    value_to_index.pop(complement)
                    # remove current num
                    value_to_index.pop(num, None)
                    # move to next number
                    continue
            
        
        # return final result
        return result
"""