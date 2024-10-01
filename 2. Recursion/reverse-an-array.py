def reverseArray(arr: list, s: int = 0):
    e = len(arr) - s - 1
    if s >= e:
        return
    # swap
    temp = arr[s]
    arr[s] = arr[e]
    arr[e] = temp

    reverseArray(arr, s + 1)


arr = [1, 2, 3, 4, 5]
reverseArray(arr)
print(arr)
