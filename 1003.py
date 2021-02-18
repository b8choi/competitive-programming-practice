t = int(input())
for i in range(t):
    n = int(input())

    cnt0 = [0 for i in range(max(2, n + 1))]
    cnt0[0] = 1
    cnt1 = [0 for i in range(max(2, n + 1))]
    cnt1[1] = 1
    for j in range(2, n + 1):
        cnt0[j] = cnt0[j - 1] + cnt0[j - 2]
        cnt1[j] = cnt1[j - 1] + cnt1[j - 2]

    print(cnt0[n], cnt1[n])
