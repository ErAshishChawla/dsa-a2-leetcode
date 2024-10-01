arr = [4, 7, 1, 1, 2, 4, 8, 11, 12, 1, 3, 4, 9, 4]
max_val = max(arr)

hash_list = []
hash_table = {}

# Hash list method using list
for i in range(max_val + 1):
    hash_list.append(0)

for i in range(len(arr)):
    hash_list[arr[i]] += 1

for i in range(len(hash_list)):
    if hash_list[i] > 0:
        print(f"{i} occurs {hash_list[i]} times")

# Hash table method using dict
for i in arr:
    if i in hash_table:
        hash_table[i] += 1
    else:
        hash_table[i] = 1

print(hash_table)
