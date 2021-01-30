t = int(input())

m = 0

tests = []
for i in range(t):
    n = int(input())
    tests.append(n)

    if  m < n:
        m = n


is_prime = [True for _ in range(m + 1)]
is_prime[0] = False
is_prime[1] = False

for i in range(2, m + 1):
    if not is_prime[i]:
        continue

    j = 2
    while i * j <= m:
        is_prime[i * j] = False
        j += 1


for n in tests:
    for i in range(int(n / 2), 1, -1):
        if is_prime[i] and is_prime[n - i]:
            print(i, n - i)
            break
