def frequencyCount(arr, N, P):
    #  do modify in the given array
    hash_list = [0] * N
    for i in arr:
        if i <= N:
            hash_list[i - 1] += 1

    for i in range(len(hash_list)):
        arr[i] = hash_list[i]
