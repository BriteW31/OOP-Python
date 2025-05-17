"""
CountingSort Algorithm
"""
class CountingSort:

    # after sort, number_list will be sorted
    @staticmethod
    def counting_sort(number_list):
        # define output array to copy later
        list_length = len(number_list)
        output_list = [0] * list_length
        
        # initialize list to count all elements
        maximum = max(number_list)
        count_list = [0] * (maximum + 1)
        
        # Store the count of each elements in count array
        for index_1 in range(0, list_length):
            count_list[number_list[index_1]] += 1

        # Store the cummulative count
        for index_2 in range(1, (maximum + 1)):
            count_list[index_2] += count_list[index_2 - 1]

        # Find the index of each element of the original array in count array
        # place the elements in output array
        index_3 = list_length - 1
        while index_3 >= 0:
            output_list[count_list[number_list[index_3]] - 1] = number_list[index_3]
            count_list[number_list[index_3]] -= 1
            index_3 -= 1
        
        # copy to number_list
        for index_4 in range(0, list_length):
            number_list[index_4] = output_list[index_4]

"""
# testing - negative numbers mess up the algorithm
test_array = [20, 12, 15, 10, 3, -6, 1, -10]
test_array_length = len(test_array)
CountingSort(test_array, test_array_length)
print(test_array)

test_array_positive = [20, 12, 15, 10, 3, 6, 1, 10]
CountingSort(test_array_positive, test_array_length)
print(test_array_positive)

test_array_2 = [4, 2, 2, 8, 3, 3, 1, 5, 6, 5, 4]
test_array_length_2 = len(test_array_2)
CountingSort(test_array_2, test_array_length_2)
print(test_array_2)
"""