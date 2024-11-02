from typing import List


def sortColors(arr: List[int]) -> None:
    # Moving ones at back and then moving twos at back
    n = len(arr)
    for i in range(1, 3):
        slow = 0
        for fast in range(n):
            if arr[slow] == i and arr[fast] != i:
                arr[slow], arr[fast] = arr[fast], arr[slow]

            if arr[slow] != i:
                slow += 1


# Using hash map
def sortColors2(arr: List[int]) -> None:
    n = len(arr)
    hash_map = {}

    for i in range(n):
        if arr[i] in hash_map:
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1

    for i in range(0, hash_map[0]):
        arr[i] = 0

    for i in range(hash_map[0], hash_map[0] + hash_map[1]):
        arr[i] = 1

    for i in range(hash_map[0] + hash_map[1], n):
        arr[i] = 2


def sortColors3(arr: List[int]) -> None:
    # Using Dutch National Flag Algorithm
    n = len(arr)
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


arr = [2, 0, 2, 1, 1, 0]
sortColors3(arr)
print(arr)  # Output: [0, 0, 1, 1, 2, 2]
