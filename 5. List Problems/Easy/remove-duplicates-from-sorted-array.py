from typing import List


def removeDuplicates(nums: List[int]) -> int:
    # l = len(nums)

    # i = 0
    # k = 1
    # while i<l-1:
    #     if nums[i] < nums[i+1]:
    #         i = i+1
    #     else:
    #         j = i+1
    #         while j < l:
    #             if nums[i] >= nums[j]:
    #                 j += 1
    #             else:
    #                 nums[i+1] = nums[j]
    #                 i+=1
    #                 break
    #         if j == l:
    #             break

    # return i+1

    hash_map = {}

    for i in nums:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1

    keys = list(hash_map.keys())

    for i in range(len(keys)):
        nums[i] = keys[i]

    return len(keys)


def removeDuplicates2(arr: List[int]):
    # We always have a unique value at the start of the array
    # We start from the second element
    swapper = 1
    for traverser in range(1, len(arr)):
        if arr[traverser] != arr[traverser - 1]:
            # it means we found a unique value and we need to copy it to the swapper
            arr[swapper] = arr[traverser]
            swapper += 1
        else:
            # it means we found a duplicate and we do not need to do anything
            continue


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
removeDuplicates2(arr)
print(arr)
