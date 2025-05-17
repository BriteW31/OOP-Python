"""
BubbleSort Algorithm Program.
"""

# Swap swaps the values of the two variables, number_one and number_two
def swap(number_list, index_one, index_two):
    # define temporary variable to hold a value to complete swap
    temp = number_list[index_one]
    number_list[index_one] = number_list[index_two]
    number_list[index_two] = temp

def bubble_sort(number_list, list_length):
    # for loop to track indexes
    for index in range(list_length):
        
        # define boolean variable to check if array changes
        mutate_list = False
        
        # compares every two elements, Swaps the values if the left value is larger than the right value
        for steps in range(0, list_length - index - 1):
            if number_list[steps] > number_list[steps + 1]:
                swap(number_list, steps, steps + 1)
                mutate_list = True
                
        # if no changes applied, breaks for loop
        if not mutate_list:
            break
        
    return number_list



