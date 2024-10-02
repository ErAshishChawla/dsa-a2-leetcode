def selectionSort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        min_index = i

        # This for loop finds minimum index in the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Always swap the minimum element with the element at the current index
        arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [4, 1, 9, 3, 2, 6]
selectionSort(arr)
print(arr)
