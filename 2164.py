from collections import deque

n = int(input())

cards = deque(range(1, n + 1))

for _ in range(n - 1):
    cards.popleft()
    first = cards.popleft()
    cards.append(first)

print(cards[0])

'''
ch = [0] * (n + 1)

d = 0
i = 1
for _ in range(n - 1):
    ch[i] = 1
    cnt = 0
    j = i
    for _ in range(n):
        j = (j % n) + 1
        if ch[j] == 0:
            cnt += 1
            if cnt == 2:
                break
    if cnt == 1:
        break
    i = j

for i in range(1, n):
    if ch[i] == 0:
        print(i)
        break
'''
