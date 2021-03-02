n = int(input())
seq = [int(x) for x in input().split()]

max_sum = -999999
summ = 0
for t in seq:
    summ += t
    if max_sum < summ:
        max_sum = summ
    if summ < 0:
        summ = 0

print(max_sum)
