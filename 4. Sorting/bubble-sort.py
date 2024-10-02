arr = [4, 1, 9, 3, 2, 6]


def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 2, -1, -1):
        swap_flag = False
        for j in range(0, i + 1):
            if arr[j] > arr[j + 1]:
                swap_flag = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swap_flag:
            break


bubbleSort(arr)
print(arr)
