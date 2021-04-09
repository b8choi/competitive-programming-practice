def find(c, d, p):
    global n
    global max_profit
    
    if d > n:
        profit = 0
        for i in range(len(c)):
            profit += w[i][1] * c[i]
        if max_profit < profit:
            max_profit = profit
    else:
        c.append(0)
        find(c, d + 1, p)
        c.pop()
        if (p < 0 or p + w[p - 1][0] - 1 < d) and d + w[d - 1][0] - 1 <= n:
            c.append(1)
            find(c, d + 1, d)
            c.pop()


n = int(input())

w = []
for i in range(n):
    t, p = [int(x) for x in input().split()]
    w.append((t, p))

max_profit = 0
find([], 1, -1)

print(max_profit)
