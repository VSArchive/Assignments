import random


def partition(arr, start, stop):
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] = arr[randpivot], arr[start]

    pivot = start
    i = start + 1

    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1

    return (pivot)


def quicksort(arr, start, stop):
    if(start < stop):
        pivotindex = partition(arr, start, stop)

        quicksort(arr, start, pivotindex-1)
        quicksort(arr, pivotindex + 1, stop)


array = []

for i in range(0, 100):
    array.append(random.randrange(0, 100))

print("Unsorted array:", array)
quicksort(array, 0, len(array) - 1)
print("Sorted array:", array)
