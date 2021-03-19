from collections import defaultdict

n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
q = [int(x) for x in input().split()]

exist = defaultdict(int)
for i in a:
    exist[i] = 1

for i in q:
    print(exist[i])
