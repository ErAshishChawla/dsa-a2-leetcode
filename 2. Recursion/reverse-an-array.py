def reverseArray(s: int, e: int, arr: list):
    if e < 0 or e >= len(arr):
        raise ("Invalid Input")

    if s < 0 or s >= len(arr):
        raise ("Invalid Input")

    if s >= e:
        return
    # swap
    temp = arr[s]
    arr[s] = arr[e]
    arr[e] = temp

    reverseArray(s + 1, e - 1, arr)


arr = [1, 2, 3, 4, 5]
reverseArray(0, len(arr) - 1, arr)
print(arr)
