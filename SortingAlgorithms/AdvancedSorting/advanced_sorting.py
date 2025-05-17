"""
Advanced Sorting Class
"""
from bucket_sort import BucketSort as Bucket
from counting_sort import CountingSort as Counting
from merge_sort import MergeSort as Merge
from quick_sort import QuickSort as Quick
from file_reader import FileReader as reader

class AdvancedSorting:
    # Bucket Sort
    def bucket_sorter(self, array):
        bucket = Bucket()
        sorted_array = bucket.bucket_sort(array)
        return sorted_array
    
    # Counting Sort
    def counting_sorter(self, array):
        Counting.counting_sort(array)
        return array
    
    # Merge Sort
    def merge_sorter(self, array):
        merging_array = Merge(array)
        size = len(array)
        sorted_array = merging_array.sort(array)
        return sorted_array
    
    # Quick Sort
    def quick_sorter(self, array):
        size = len(array)
        Quick().quick_sort(array, 0, size - 1)
        return array
    
    # Print Product
    def printer(self, array):
        for i in range(len(array) - 1):
            print(array[i], end=", ")
        print(array[len(array) - 1]) 
    
    # Copy Data
    def copy_array(self, array):
        copy_array = []
        for index in range(len(array)):
            copy_array.append(array[index])
        return copy_array    


if __name__ == "__main__":
    advanced_sort = AdvancedSorting()
    # data set 1 - integers
    data = reader().read_file("")
    print(data)
    # data set 2 - decimals
    data_2 = reader().read_file("decimal.txt")
    print(data_2)
    # data set 3 - positive integers
    data_3 = reader().read_file("number_positive.txt")
    print(data_3)
    print("\nBucket Sort Start: ")
    
    # bucket sort uses data set 2
    bucket_sort_result = advanced_sort.bucket_sorter(advanced_sort.copy_array(data_2))
    print(bucket_sort_result)
    print(data_2)    
    print("\nCounting Sort Start: ")
    
    # counting sort uses data set 3
    counting_sort_result = advanced_sort.counting_sorter(advanced_sort.copy_array(data_3))
    print(counting_sort_result)
    print(data_3)     
    print("\nQuick Sort Start:")
    
    # quick sort can sort all three
    quick_sort_result = advanced_sort.quick_sorter(advanced_sort.copy_array(data))
    print(quick_sort_result)
    print(data)     
    print("\n")
    
    quick_sort_result_2 = advanced_sort.quick_sorter(advanced_sort.copy_array(data_2))
    print(quick_sort_result_2)
    print(data_2)     
    print("\n")  
    
    quick_sort_result_3 = advanced_sort.quick_sorter(advanced_sort.copy_array(data_3))
    print(quick_sort_result_3)
    print(data_3)     
    print("\nMerge Sort Start:")
    
    # merge sort can sort all three
    merge_sort_result = advanced_sort.merge_sorter(advanced_sort.copy_array(data))
    print(merge_sort_result)
    print(data)     
    print("\n")    
    
    merge_sort_result_2 = advanced_sort.merge_sorter(advanced_sort.copy_array(data_2))
    print(merge_sort_result_2)
    print(data_2)     
    print("\n") 
    
    merge_sort_result_3 = advanced_sort.merge_sorter(advanced_sort.copy_array(data_3))
    print(merge_sort_result_3)
    print(data_3)     
    print("\n")     
    
    
