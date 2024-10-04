def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def mergeSort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


arr = [12, 11, 13, 5, 6, 7]
print("Given array is", arr)
arr = mergeSort(arr)
print("Sorted array is: ", arr)
