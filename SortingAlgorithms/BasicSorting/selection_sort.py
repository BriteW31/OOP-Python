"""
SelectionSort Algorithm
"""
# Swap swaps the values of the two variables, number_one and number_two
def swap(number_list, index_one, index_two):
    # define temporary variable to hold a value to complete swap
    temp = number_list[index_one]
    number_list[index_one] = number_list[index_two]
    number_list[index_two] = temp

def selection_sort(number_list, list_length):
    # for loop to track indexes
    for index in range(list_length):
        
        # initialize i-th element of list as index with smallest value
        min_index = index
        
        # for loop to determine index holding smallest value
        for steps in range(index + 1, list_length):
            # sets index to steps, which has smaller value, if it exists
            if number_list[steps] < number_list[min_index]:
                min_index = steps
                
        # Swaps the i-th value and the smallest value
        swap(number_list, index, min_index)

    return number_list
