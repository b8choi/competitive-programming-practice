N = 100

t = int(input())

# 이전 길이 + -5 길이
side = [0] * (N + 1)
side[1] = 1
side[2] = 1
side[3] = 1
side[4] = 2
side[5] = 2
for i in range(6, N + 1):
    side[i] = side[i - 1] + side[i - 5]

for i in range(t):
    n = int(input())
    print(side[n])
