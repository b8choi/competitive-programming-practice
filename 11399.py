n = int(input())
p = [int(x) for x in input().split()]

p.sort()

summ = 0
for i in range(n):
    summ += sum(p[:i + 1])

print(summ)
