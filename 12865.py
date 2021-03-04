n, k = [int(x) for x in input().split()]
weights = [0]
values = [0]
for i in range(n):
    w, v = [int(x) for x in input().split()]
    weights.append(w)
    values.append(v)

mx = [[0] * (n + 1) for _ in range(k + 1)]
for i in range(1, k + 1):
    for j in range(1, n + 1):
        before = 0
        if i - weights[j] >= 0:
            before = mx[i - weights[j]][j - 1] + values[j]
        mx[i][j] = max(before, mx[i][j - 1]) #max(mx[i - weights[j]][:j]) + values[j]

#for row in mx:
#    print(row)
print(max(mx[k]))
