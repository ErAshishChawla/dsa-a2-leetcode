from typing import List


def removeDuplicates(self, nums: List[int]) -> int:
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
