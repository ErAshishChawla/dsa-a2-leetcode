from typing import *


def countFrequency(n: int, m: int, edges: List[int]):
    hash_list = [0] * n

    for i in edges:
        if i > n:
            continue
        else:
            hash_list[i - 1] += 1

    return hash_list
