n, m, v = input().split()
n = int(n)
m = int(m)
v = int(v)

g = []
for i in range(n + 1):
    row = []
    for j in range(n + 1):
        row.append(False)
    g.append(row)

visited = []
for i in range(n + 1):
    visited.append(False)

for i in range(m):
    a, b = input().split()
    a = int(a)
    b = int(b)
    g[a][b] = g[b][a] = True


def dfs(v):
    global n
    global g, visited

    print(v, end=' ')

    for i in range(n + 1):
        if g[v][i] == True and visited[i] == False:
            visited[i] = True
            dfs(i)


def bfs(v):
    global n
    global g, visited

    q = []

    q.append(v)
    while len(q) > 0:
        cur = q.pop(0)
        print(cur, end=' ')
        for i in range(n + 1):
            if g[cur][i] == True and visited[i] == False:
                visited[i] = True
                q.append(i)


visited[v] = True
dfs(v)
print()

visited = []
for i in range(n + 1):
    visited.append(False)

visited[v] = True
bfs(v)
