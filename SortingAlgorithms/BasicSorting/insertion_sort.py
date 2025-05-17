"""
InsertionSort Algorithm
"""

def InsertionSort(number_list, list_length): 
    # for loop to track indexes
    for index in range(1, list_length):
        
        # assume one value is already sorted
        temp = number_list[index]        
        steps = index - 1
        
        # while loop to organize all values greater than temp
        while steps >= 0 and temp < number_list[steps]:
            number_list[steps + 1] = number_list[steps]
            steps = steps - 1
            
        # set the element that is greater than temp the value of temp
        number_list[steps + 1] = temp
        
    return number_list

