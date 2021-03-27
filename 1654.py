import sys
import math
from collections import deque

n, k = [int(x) for x in input().split()]

cables = deque()
total = 0
longest = 0
for i in range(n):
    l = int(sys.stdin.readline()[:-1])
    cables.append(l)
    total += l
    if longest < l:
        longest = l

upper = int(math.ceil(total / k))
lower = int(longest / k)
#print(lower, upper)

def getSegments(unit):
    s = 0
    for c in cables:
        s += c // int(unit)
    return s


while True:
    mid = int((lower + upper) / 2)
    if mid == 0:
        mid = 1

    s = getSegments(mid)
    #print(s, lower, mid, upper)
    #print(getSegments(mid), getSegments(mid + 1))

    if getSegments(mid) >= k and getSegments(mid + 1) < k:
        print(int(mid))
        break
    elif s < k:
        upper = mid - 1
    else:
        lower = mid + 1
