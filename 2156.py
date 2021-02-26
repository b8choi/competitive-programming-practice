n = int(input())

q = []
for i in range(n):
    q.append(int(input()))

d = [[0, 0, 0] for _ in range(n)]
d[0][1] = q[0]

for i in range(1, n):
    d[i][0] = max(d[i - 1][0], d[i - 1][1], d[i - 1][2])
    d[i][1] = d[i - 1][0] + q[i]
    d[i][2] = d[i - 1][1] + q[i]

#for i in range(n):
#    print(q[i], d[i])
print(max(d[-1]))
