from typing import List


def rotateRightByK(arr: List[int], k: int) -> None:
    n = len(arr)
    rotations = k % n
    if rotations > 0:
        rotated_arr = [0] * n
        for i in range(n):
            new_index = (i + rotations) % n
            rotated_arr[new_index] = arr[i]
        for i in range(n):
            arr[i] = rotated_arr[i]


def rightRotateByK2(arr: List[int], k: int):
    n = len(arr)
    rotations = k % n

    if rotations == 0:
        return

    rotated_arr = [0] * n
    for i in range(n):
        new_idx = (i + rotations) % n
        rotated_arr[new_idx] = arr[i]
    arr[:] = rotated_arr


def reverseSubArray(arr: List[int], start: int, end: int):
    i = start
    j = end

    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def rightRotateByK3(arr: List[int], k: int):
    # It will take two stages
    n = len(arr)
    # 1. Reverse the whole array
    reverseSubArray(arr, 0, n - 1)

    # 2. Reverse the 0 to k-1 elements
    reverseSubArray(arr, 0, k - 1)
    # 3. Reverse the k to n-1 elements
    reverseSubArray(arr, k, n - 1)


arr = [1, 3, 5, 7, 9]
print(arr)

rotateRightByK(arr, 3)
print(arr)

arr = [1, 3, 5, 7, 9]
rightRotateByK2(arr, 3)
print(arr)

arr = [1, 3, 5, 7, 9]
rightRotateByK3(arr, 3)
print(arr)
