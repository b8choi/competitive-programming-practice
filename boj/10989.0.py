n = int(input())

cnt = []
for i in range(10001):
    cnt.append(0)

for i in range(n):
    k = int(input())
    cnt[k] += 1

for i in range(1, 10001):
    for j in range(cnt[i]):
        print(i)
