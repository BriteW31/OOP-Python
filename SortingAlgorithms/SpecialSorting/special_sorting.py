"""
Special Sorting
"""

from heap_sort import HeapSort as Heap
from radix_sort import RadixSort as Radix
from shell_sort import ShellSort as Shell
from tree_sort import TreeSort as Tree
from file_reader import FileReader as reader

class SpecialSorting:
    # Heap Sort
    def heap_sorter(self, array):
        heap = Heap(array)
        sorted_array = heap.heap_sort(len(array))
        return sorted_array
    
    # Radix Sort
    def radix_sorter(self, array):
        radix = Radix(array)
        sorted_array = radix.radix_sort()
        return sorted_array
    
    # Shell Sort
    def shell_sorter(self, array):
        Shell.shell_sort(array, len(array))
        return array
    
    # Tree Sort
    def tree_sorter(self, array):
        tree = Tree()
        tree.sort(array)
        sorted_array = []
        tree.append_binary_tree(tree.root, sorted_array)
        return sorted_array
    
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


# testing
if __name__ == "__main__":
    special_sort = SpecialSorting()
    # data set 1 - integers
    data = reader().read_file("")
    print(data)    
    #data set 2 - positive integers
    data_2 = reader().read_file("number_positive.txt")
    print(data_2)
    print("\nRadix Sort Result: ")
    
    # Radix Sort sorts only data set 2
    radix_sort_result = special_sort.radix_sorter(special_sort.copy_array(data_2))
    print(data_2)
    print(radix_sort_result)
    special_sort.printer(radix_sort_result)
    print("\n")
    
    # Heap Sort can sort both
    print("\n Heap Sort Result:")
    heap_sort_result = special_sort.heap_sorter(special_sort.copy_array(data))
    print(data)
    print(heap_sort_result)
    special_sort.printer(heap_sort_result)
    print("\n")
    
    heap_sort_result_2 = special_sort.heap_sorter(special_sort.copy_array(data_2))
    print(data_2)
    print(heap_sort_result_2)
    special_sort.printer(heap_sort_result_2)
    print("\n")
    
    # Shell Sort can sort both
    print("\n Shell Sort Result:")
    shell_sort_result = special_sort.shell_sorter(special_sort.copy_array(data))
    print(data)
    print(shell_sort_result)
    special_sort.printer(shell_sort_result)
    print("\n")
    
    shell_sort_result_2 = special_sort.shell_sorter(special_sort.copy_array(data_2))
    print(data_2)
    print(shell_sort_result_2)
    special_sort.printer(shell_sort_result_2)
    print("\n")   
    
    # Tree Sort can sort both
    print("\n Tree Sort Result:")
    tree_sort_result = special_sort.tree_sorter(special_sort.copy_array(data))
    print(data)
    print(tree_sort_result)
    special_sort.printer(tree_sort_result)
    print("\n")
    
    tree_sort_result_2 = special_sort.tree_sorter(special_sort.copy_array(data_2))
    print(data_2)
    print(tree_sort_result_2)
    special_sort.printer(tree_sort_result_2)
    print("\n")    