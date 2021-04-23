from sys import stdin
import math

n = int(input())
m = int(input())

cost = [([math.inf] * n) for _ in range(n)]
for _ in range(m):
    p, q, c = [int(x) for x in stdin.readline().split()]
    if cost[p - 1][q - 1] > c:
        cost[p - 1][q - 1] = c

a, b = [(int(x) - 1) for x in input().split()]


dist = [math.inf] * n
visited = [0] * n

dist[a] = 0
for k in range(n):
    min_val = math.inf
    min_idx = 0
    for i in range(n):
        if not visited[i] and min_val > dist[i]:
            min_val = dist[i]
            min_idx = i
    visited[min_idx] = 1

    for i in range(n):
        if not visited[i] and dist[i] > min_val + cost[min_idx][i]:
            dist[i] = min_val + cost[min_idx][i]


print(dist[b])
