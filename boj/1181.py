import sys

n = int(input())

strings = []
for i in range(n):
    s = input()
    strings.append(s)

strings = list(set(strings))
strings.sort()
strings.sort(key=lambda x: len(x))

for s in strings:
    print(s)
