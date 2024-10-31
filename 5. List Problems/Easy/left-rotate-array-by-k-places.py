def leftRotate(arr, k):
    # Bruteforce approach
    n = len(arr)

    if k % n == 0:
        return arr

    rotations = k % n
    while rotations > 0:
        key = arr[0]
        for i in range(0, n - 1):
            arr[i] = arr[i + 1]
        arr[n - 1] = key
        rotations -= 1


def leftRotate2(arr, k):
    # Better approach,
    # Uses extra space
    n = len(arr)
    rotations = k % n

    if rotations == 0:
        return arr

    rotated_arr = [0] * n

    for i in range(n):
        new_index = (i - rotations) % n
        rotated_arr[new_index] = arr[i]

    return rotated_arr


def rotateSubArray(arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def leftRotate3(arr, k):
    # Best approach
    # Uses reverse algorithm

    n = len(arr)

    # Reverse the whole array
    rotateSubArray(arr, 0, n - 1)

    # Reverse the elements from 0 to k(inclusive)
    rotateSubArray(arr, 0, k)

    # Reverse the elements from k + 1 to n - 1(inclusive)
    rotateSubArray(arr, k + 1, n - 1)


arr = [1, 3, 5, 7, 9]
print(arr)
leftRotate(arr, 3)
print(arr)

arr = [1, 3, 5, 7, 9]
print(leftRotate2(arr, 3))

arr = [1, 3, 5, 7, 9]
leftRotate3(arr, 3)
