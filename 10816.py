from collections import defaultdict

n = int(input())
cards = [int(x) for x in input().split()]
m = int(input())
targets = [int(x) for x in input().split()]

cnt = defaultdict(int)
for c in cards:
    cnt[c] += 1

for t in targets:
    print(cnt[t], end=' ')
