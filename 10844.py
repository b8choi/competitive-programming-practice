N = 100
LIM = 1000000000

n = int(input())

c = [[]]
for i in range(1, n + 1):
    row = [0] * 10
    c.append(row)
for i in range(1, 10):
    c[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        down = 0
        if j > 0:
            down = c[i - 1][j - 1]
        up = 0
        if j < 9:
            up = c[i - 1][j + 1]

        c[i][j] = (down + up) % LIM

print(sum(c[-1]) % LIM)
