nums = [1,1,1,2,2,3]
k = 2
counts = {}

for num in nums:
    if num not in counts:
        counts[num] = 1
    else:
        counts[num] += 1

sorted_keys = sorted(counts, key=counts.get, reverse=True)

result = sorted_keys[:k]
print(result)