N = 300

n = int(input())

steps = [0]
for i in range(n):
    score = int(input())
    steps.append(score)

summ = [[0, 0] for _ in range(n + 1)]
summ[0][0] = summ[0][1] = 0
summ[1][0] = steps[1]
summ[1][1] = 0
for i in range(2, n + 1):
    summ[i][0] = max(summ[i - 2]) + steps[i]
    summ[i][1] = summ[i - 1][0] + steps[i]

print(max(summ[-1]))
