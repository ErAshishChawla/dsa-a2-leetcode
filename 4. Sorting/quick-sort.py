def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j


def quickSort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)
        left = quickSort(arr, low, pi - 1)
        right = quickSort(arr, pi + 1, high)
