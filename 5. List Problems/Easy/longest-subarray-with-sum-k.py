def lenOfLongestSubarr(arr, k):
    # Prefix sum
    max_len = 0
    sum_map = {}
    total = 0
    for i in range(len(arr)):
        total = total + arr[i]
        if total == k:
            max_len = i + 1
        rem = total - k
        if rem in sum_map:
            max_len = max(max_len, i - sum_map[rem])
        if total not in sum_map:
            sum_map[total] = i
    return max_len
