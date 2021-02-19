n = int(input())

costs = []
for i in range(n):
    cost = [int(x) for x in input().split()]
    costs.append(cost)

min_cost = [[0, 0, 0] for _ in range(n)]
min_cost[0] = costs[0]
for i in range(1, n):
    min_cost[i][0] = min(min_cost[i - 1][1] + costs[i][0], min_cost[i - 1][2] + costs[i][0])
    min_cost[i][1] = min(min_cost[i - 1][0] + costs[i][1], min_cost[i - 1][2] + costs[i][1])
    min_cost[i][2] = min(min_cost[i - 1][0] + costs[i][2], min_cost[i - 1][1] + costs[i][2])

print(min(min_cost[-1]))
