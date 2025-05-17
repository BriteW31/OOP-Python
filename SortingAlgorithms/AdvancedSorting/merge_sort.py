"""
MergeSort Algorithm
"""

# Alternate MergeSort - Class
class MergeSort:
    def __init__(self, array):
        self.array = array
        
    def merger(self, left, right):
        merge_array = []
        left_index = 0
        right_index = 0
        
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merge_array.append(left[left_index])
                left_index += 1
            else:
                merge_array.append(right[right_index])
                right_index += 1
        
        merge_array.extend(left[left_index:])
        merge_array.extend(right[right_index:])
        return merge_array
    
    
    def divider(self, array):
        size = len(array)
        mid = size // 2
        return array[:mid], array[mid:]
        
    
    def merge_sort_three(self, array = None):
        if array is None:
            array = self.array
            
        if len(array) <= 1:
            return array
        
        left, right = self.divider(array)
        sort_left = self.merge_sort_three(left)
        sort_right = self.merge_sort_three(right)
        
        return self.merger(sort_left, sort_right)
    
    def sort(self, array):
        self.array = self.merge_sort_three()
        
        return self.array  


"""
is_left_ready = False
is_right_reay = False

def merge_sort(number_list, list_length):
    # creates sublists of numbers by cutting in half
    if list_length > 1:
        half_index = list_length // 2
        left_list = number_list[half_index:]
        right_list = number_list[:half_index]
        
        # define variables for lengths of sublists
        left_list_length = len(left_list)
        right_list_length = len(right_list)   
        
        # recursive call for left, right lists
        merge_sort(left_list, left_list_length)
        merge_sort(right_list, right_list_length)
    
        # initialize all indexes, left, right, and main lists
        left_index = 0
        right_index = 0
        index = 0
    
        # while loop to add all sublists to the main list
        while left_index < left_list_length and right_index < right_list_length:
            # if left list's position has a smaller value, then add it first
            if left_list[left_index] < right_list[right_index]:
                number_list[index] = left_list[left_index]
                left_index = left_index + 1
                # if right list's position has a smaller value, add it first
            else:
                number_list[index] = right_list[right_index]
                right_index = right_index + 1
            # increases index
            index = index + 1
        
        # adds remaining elements of left list
        while left_index < left_list_length:
            number_list[index] = left_list[left_index]
            left_index = left_index + 1    
            index = index + 1
        
        # adds remaining elements of right list
        while right_index < right_list_length:
            number_list[index] = right_list[right_index]
            right_index = right_index + 1    
            index = index + 1

# Alternate MergeSort - failed
def merge_sort_two(number_list, list_length):
    # creates sublists of numbers by cutting in half
    if list_length > 1:
        half_index = list_length // 2
        left_list = number_list[half_index:]
        right_list = number_list[:half_index]
        
        # define variables for lengths of sublists
        left_list_length = len(left_list)
        right_list_length = len(right_list)   
        
        # recursive call for left, right lists
        merge_sort_two(left_list, left_list_length)
        merge_sort_two(right_list, right_list_length)
    
        # initialize all indexes, left, right, and main lists
        left_index = 0
        right_index = 0
        index = 0
    
        # while loop to add all sublists to the main list
        while left_index < left_list_length and right_index < right_list_length:
            # if left list's position has a smaller value, then add it first
            if left_list[left_index] < right_list[right_index]:
                number_list[index] = left_list[left_index]
                left_index = left_index + 1
                # if right list's position has a smaller value, add it first
            else:
                number_list[index] = right_list[right_index]
                right_index = right_index + 1
            # increases index
            index = index + 1
        
        # determine which list, left or right, is still remaining, adds it to list
        if left_index < left_list_length:
            return number_list[:index] + left_list[left_index:]
        else:
            return number_list[:index] + right_list[right_index:]
"""

      
    

"""
def divide(array):
    if len(array) > 1:
        half = len(array) // 2
        left = array[:half]
        right = array[half:]
        
        return {left: array[:half], right: array[half:]}
    else:
        return {left: array, right: []}

def divide_and_merge(left_array, right_array):
    if len(left_array) < 2 and len(right_array) < 2:
        return merge(left_array, right_array)
    else:
        if len(left_array) == 1:
            divide_result = divide(right_array)
            merged_right = merge(divide_left, divide_right)
            return merge(left_array, merged_right)
        else:
            left = divide(left_array)
            right = divide(right_array)
            result_a = divide_and_merge(left['left'], left['right'])
            result_b = divide_and_merge(right['left'], right['right'])
            return merge(result_a, result_b)

# testing
test_array_1 = [1, 2, 3, 5, 9, 1, 3, 5, -2, 5, 7, 10, 100, 9, 89, 64, 2]
array = MergeSort(test_array_1)
sort = array.sort(test_array_1)
print(sort)

test_array_2 = [1, 2, 3, 5, 9, 1, 3, 5, -2, 5, 7, 10, 100, 9, 89, 64, 2]
sort = merge_sort_two(test_array_2, len(test_array_2))
print(sort)

test_array_3 = [1, 2, 3, 5, 9, 1, 3, 5, -2, 5, 7, 10, 100, 9, 89, 64, 2]
merge_sort(test_array_3, len(test_array_3))
print(test_array_3)

# testing
test_array_1 = [1, 2, 3, 5, 9, 1, 3, 5, -2, 5, 7, 10, 100, 9, 89, 64, 2]
sort = merge_sort_three(test_array_1)
print(sort)

# testing
test_array_1 = [20, 12, 15, 10, 11, 3, -6, 1, -10]
test_array_length = len(test_array_1)
MergeSort(test_array_1, test_array_length)
print(test_array_1)
test_array_2 = [20, 12, 15, 10, 11, 3, -6, 1, -10]
test_array_length_2 = len(test_array_2)
sorted_test_2 = MergeSortTwo(test_array_2, test_array_length_2)
print("----")
print(sorted_test_2)
"""