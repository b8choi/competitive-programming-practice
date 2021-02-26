n = int(input())
a = [int(x) for x in input().split()]

d = [1] * n
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

print(max(d))
