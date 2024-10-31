def mergeTwoSortedArrays(arr1, arr2):
    l = 0
    r = 0

    result = []

    while l < len(arr1) and r < len(arr2):
        if arr1[l] <= arr2[r]:
            if len(result) == 0 or result[-1] != arr1[l]:
                result.append(arr1[l])
            l += 1
        else:
            if len(result) == 0 or result[-1] != arr2[r]:
                result.append(arr2[r])
            r += 1

    for i in range(l, len(arr1)):
        if result[-1] != arr1[i]:
            result.append(arr1[i])

    for i in range(r, len(arr2)):
        if result[-1] != arr2[i]:
            result.append(arr2[i])

    return result


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 5, 6, 7]
print(mergeTwoSortedArrays(arr1, arr2))
