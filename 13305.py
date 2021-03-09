n = int(input())
dists = [int(x) for x in input().split()]
prices = [int(x) for x in input().split()][:-1]

total = 0
min_price = prices[0]
for i in range(n - 1):
    if min_price > prices[i]:
        min_price = prices[i]
    total += min_price * dists[i]

print(total)
