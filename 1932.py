n = int(input())

summ = []

triangle = []
for i in range(n):
    line = [int(x) for x in input().split()]
    triangle.append(line)
    summ.append([0] * (i + 1))

summ[0][0] = triangle[0][0]
for i in range(1, n):
    for j in range(i + 1):
        left = 0
        if j > 0:
            left = summ[i - 1][j - 1]
        
        right = 0
        if j < i:
            right = summ[i - 1][j]

        summ[i][j] = max(left, right) + triangle[i][j]

print(max(summ[-1]))
