import sys
sys.setrecursionlimit(10000)


ox = [1, 0, -1, 0]
oy = [0, 1, 0, -1]

def fill(field, y, x, w, h):
    field[y][x] *= -1

    for i in range(4):
        nx = x + ox[i]
        ny = y + oy[i]
        if (nx >= 0 and nx < m) and (ny >= 0 and ny < n) and field[ny][nx] > 0:
            fill(field, ny, nx, w, h)


t = int(input())
for _ in range(t):
    m, n, k = [int(x) for x in input().split()]

    field = [([0] * m) for _ in range(n)]
    for _ in range(k):
        x, y = [int(x) for x in input().split()]
        field[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] > 0:
                cnt += 1
                fill(field, i, j, m, n)

    print(cnt)
