"""
Median Stream, using Insertion
"""

def getMedian(arr):
    res = []

    res.append(float(arr[0]))

    for i in range(1, len(arr)):
        j = i - 1
        num = arr[i]

        # shift elements to right to create space to insert
        # the current element at its correct position
        while j >= 0 and arr[j] > num:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = num

        length = i + 1

        # If odd number of integers are read from stream
        # then middle element in sorted order is median
        # else average of middle elements is median
        if length % 2 != 0:
            median = arr[length // 2] / 1
        else:
            median = (arr[(length // 2) - 1] + arr[length // 2]) / 2.0

        res.append(median)

    return res

if __name__ == '__main__':
    arr = [5, 15, 1, 3, 2, 8]
    res = getMedian(arr)

    print(res)