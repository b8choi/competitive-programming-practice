t = int(input())
for _ in range(t):
    a = [int(x) for x in input().split()]
    a.sort()
    print(a[-3])
