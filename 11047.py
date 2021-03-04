n, k = [int(x) for x in input().split()]

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.reverse()

cnt = 0
for c in coins:
    if k >= c:
        cnt += k // c
        k %= c

print(cnt)
