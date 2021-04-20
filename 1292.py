a, b = [int(x) for x in input().split()]

summ = 0

n = 0
i = 0
while i < b:
    n += 1
    for _ in range(n):
        i += 1
        if a <= i and i <= b:
            summ += n
        if i == b:
            break

print(summ)
