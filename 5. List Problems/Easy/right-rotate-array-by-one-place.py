def rightRotateByOne(arr):
    n = len(arr)
    key = arr[n - 1]
    for i in range(n - 2, -1, -1):
        arr[i + 1] = arr[i]
    arr[0] = key
