s = input()
t = input()

ls = len(s)
lt = len(t)

lcs = [[0 for _ in range(lt + 1)] for _ in range(ls + 1)]

for i in range(1, ls + 1):
    for j in range(1, lt + 1):
        if s[i - 1] == t[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

print(lcs[ls][lt])
