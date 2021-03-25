n, k = [int(x) for x in input().split()]

nums = list(range(1, n + 1))

result = []

i = 0
for _ in range(n):
    i = (i + k - 1) % len(nums)
    result.append(str(nums[i]))
    nums.pop(i)

print('<' + ', '.join(result) + '>')
