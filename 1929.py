m, n = [int(x) for x in input().split()]

divided = [0 for _ in range(n + 1)]
divided[1] = 1

for i in range(2, n + 1):
    if divided[i] == 0:
        j = 2
        while i * j <= n:
            divided[i * j] = 1
            j += 1

for i in range(m, n + 1):
    if divided[i] == 0:
        print(i)
