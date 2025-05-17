"""
BucketSort Algorithm
"""

class BucketSort:
    def __init__(self):
        self.__bucket = []

    def __build_bucket(self, size):
        # create buckets in bucket array
        for bucket_index in range(size):
            self.__bucket.append([])

    def __sort_buckets(self):
        # sort all buckets
        for index in range(len(self.__bucket)):
            self.__bucket[index] = sorted(self.__bucket[index])

    def bucket_sort(self, number_list):
        # initialize bucket array
        self.__bucket = []
        list_length = len(number_list)
        
        self.__build_bucket(list_length)
        
        # place numbers in their buckets
        for number in number_list:
            number_index = int(list_length * number)
            self.__bucket[number_index].append(number)
        
        self.__sort_buckets()
        
        # copy buckets into number_list
        counter = 0
        for index_1 in range(list_length):
            for index_2 in range(len(self.__bucket[index_1])):
                number_list[counter] = self.__bucket[index_1][index_2]
                counter += 1
        
        # return sorted number_list
        return number_list

"""
# testing - negative numbers do not work, need to be decimals
test_array = [0.20, 0.12, 0.15, 0.10, 0.11, 0.3, -0.6, 0.1, -0.19]
test_array_length = len(test_array)
sorted_array = BucketSort(test_array, test_array_length)
print(sorted_array)

test_array_positive = [0.20, 0.12, 0.15, 0.10, 0.11, 0.3, 0.6, 0.1, 0.19]
sorted_array_2 = BucketSort(test_array_positive, test_array_length)
print(sorted_array_2)
"""