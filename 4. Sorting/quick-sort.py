# def partition(arr, low, high):
#     pivot = arr[low]
#     i = low
#     j = high

#     while i < j:
#         while arr[i] <= pivot and i <= high - 1:
#             i += 1
#         while arr[j] > pivot and j >= low + 1:
#             j -= 1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[low], arr[j] = arr[j], arr[low]

#     return j


# def quickSort(arr, low=0, high=None):
#     if high is None:
#         high = len(arr) - 1

#     if low < high:
#         pi = partition(arr, low, high)
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)


def quickSort(arr, low, high):
    if low < high:
        i = low
        j = high

        pivot = arr[low]

        while i < j:
            while not arr[i] > pivot:
                i += 1
                if i == high:
                    break

            while not arr[j] < pivot:
                j -= 1
                if j == low:
                    break

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[j], arr[low] = arr[low], arr[j]

        quickSort(arr, low, j - 1)
        quickSort(arr, j + 1, high)


# arr = [12, 8, 7, 2, 6, 9, 3, 12]
arr = [12, 12, 12, 12, 12, 12, 12, 12]
quickSort(arr, 0, 7)
print(arr)
