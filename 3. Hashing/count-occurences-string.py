s = "abcccabdfg"

# Method 1: Using Hash Map
hash_map = {}

for i in s:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map[i] = 1

min_ascii = ord(min(s))
max_ascii = ord(max(s))
difference = max_ascii - min_ascii + 1

# Method 2: Using Hash List
hash_list = [0] * difference

for i in s:
    idx = ord(i) - min_ascii
    hash_list[idx] += 1

print(hash_map)
print(hash_list)
