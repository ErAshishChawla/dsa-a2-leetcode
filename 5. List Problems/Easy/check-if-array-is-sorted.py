from typing import List


def check(self, arr: List[int]) -> bool:
    # b_index = -1
    # is_broken = False
    # for i in range(0, len(arr)-1):
    #     if arr[i] > arr[i+1]:
    #         b_index = i+1
    #         is_broken = True
    #         break
    # if not is_broken:
    #     return True
    # c_b_index = b_index - len(arr)
    # for i in range(0, c_b_index,-1):
    #     if arr[i] < arr[i-1]:
    #         return False
    # return True
    drops = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            drops += 1
    if arr[0] < arr[len(arr) - 1]:
        drops += 1
    return drops <= 1
