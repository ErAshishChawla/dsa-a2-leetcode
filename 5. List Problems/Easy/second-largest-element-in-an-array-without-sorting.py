def getSecondOrderElements(n: int, a: [int]) -> [int]:
    # Write your code here.

    largest = float("-inf")
    s_largest = float("-inf")
    smallest = float("inf")
    s_smallest = float("inf")

    for i in a:
        if i > largest:
            s_largest = largest
            largest = i
        elif i > s_largest and i != largest:
            s_largest = i

        if i < smallest:
            s_smallest = smallest
            smallest = i
        elif i < s_smallest and i != smallest:
            s_smallest = i
    return [s_largest, s_smallest]
