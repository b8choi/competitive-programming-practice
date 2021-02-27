C = 500
N = 100

c = [0 for _ in range(C + 1)]

n = int(input())
for _ in range(n):
    a, b = [int(x) for x in input().split()]
    c[a] = b

d = [0] * (C + 1)
for i in range(1, C + 1):
    for j in range(0, i):
        if c[j] < c[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

print(n - max(d))
