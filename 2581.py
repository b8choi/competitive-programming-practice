m = int(input())
n = int(input())

divided = [0 for _ in range(n + 1)]
divided[0] = 1
divided[1] = 1

for i in range(2, n + 1):
    if not divided[i]:
        for j in range(i + 1, n + 1):
            if j % i == 0:
                divided[j] = 1

first_prime = None
sum_prime = 0
for i in range(m, n + 1):
    if not divided[i]:
        if first_prime == None:
            first_prime = i
        sum_prime += i

if first_prime == None:
    print('-1')
else:
    print(sum_prime)
    print(first_prime)
