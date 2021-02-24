INF = 99999999

n = int(input())

d = [INF] * (n + 1)
d[1] = 0

for i in range(1, n):
    if i * 2 <= n and d[i * 2] > d[i] + 1:
        d[i * 2] = d[i] + 1
    if i * 3 <= n and d[i * 3] > d[i] + 1:
        d[i * 3] = d[i] + 1
    if d[i + 1] > d[i] + 1:
        d[i + 1] = d[i] + 1

print(d[n])
