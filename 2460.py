m = 0
total = 0
for _ in range(10):
    o, i = [int(x) for x in input().split()]
    total += i - o
    if m < total:
        m = total

print(m)
