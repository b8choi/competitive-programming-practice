n = int(input())
a = [int(x) for x in input().split()]

d = [1] * n
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

e = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if a[i] > a[j] and e[i] < e[j] + 1:
            e[i] = e[j] + 1

b = 1
for i in range(n):
    if b < d[i] + e[i] - 1:
        b = d[i] + e[i] - 1

print(b)
