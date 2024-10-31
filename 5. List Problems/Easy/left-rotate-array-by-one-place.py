def rotateArrayByOne(arr):
    n = len(arr)
    key = arr[0]

    for i in range(0, n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = key


arr = [1, 2, 3, 4, 5]
rotateArrayByOne(arr)
print(arr)
