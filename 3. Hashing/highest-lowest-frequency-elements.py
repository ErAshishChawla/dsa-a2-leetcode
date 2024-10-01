from typing import List


def getFrequencies(v: List[int]) -> List[int]:
    # Write your code here
    hash_map = {}

    for i in v:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1

    min_ele = float("inf")
    min_freq = float("inf")
    max_ele = float("-inf")
    max_freq = float("-inf")

    for k, v in hash_map.items():
        if v > max_freq or (v == max_freq and k < max_ele):
            max_ele, max_freq = k, v

        if v < min_freq or (v == min_freq and k < min_ele):
            min_ele, min_freq = k, v

    return [max_ele, min_ele]
