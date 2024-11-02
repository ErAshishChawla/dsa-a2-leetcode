from typing import List

def moveZeroes(arr: List[int]) -> None:
    n = len(arr)
    slow = 0
    for fast in range(n):
        if arr[slow] == 0 and arr[fast] !=0:
            arr[slow],arr[fast] = arr[fast],arr[slow]
        
        if arr[slow]!=0:
            slow+=1

arr = [0, 1, 0, 3, 12]
moveZeroes(arr)
        
