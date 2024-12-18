from typing import List


# My Solution:
def majorityElement(arr: List[int]) -> int | None:
    n = len(arr)
    limit = n // 2

    count = {}

    for i in arr:
        if i in count:
            count[i] += 1

        else:
            count[i] = 1

        if count[i] > limit:
            return i


test_case_1 = [3, 2, 3]
test_case_2 = [2, 2, 1, 1, 1, 2, 2]

print(majorityElement(test_case_1))  # 3
print(majorityElement(test_case_2))  # 2


# Optimal Solution:
# Moore's Voting Algorithm
def majorityElement2(arr: List[int]) -> int:
    n = len(arr)

    count = 0
    candidate = arr[0]

    for i in range(n):
        if arr[i] == candidate:
            count += 1
        else:
            count -= 1

        if count == 0:
            candidate = arr[i]
            count = 1

    # Count the candidate Only to be sure
    candidate_count = 0
    for i in arr:
        if i == candidate:
            candidate_count += 1

    return candidate if candidate_count > n // 2 else 0


test_case_1 = [3, 2, 3]
test_case_2 = [2, 2, 1, 1, 1, 2, 2]

print(majorityElement2(test_case_1))  # 3
print(majorityElement2(test_case_2))  # 2
