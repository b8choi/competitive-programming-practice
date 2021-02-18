max_n = 0

tests = []
while True:
    n = int(input())
    if n == 0:
        break
    tests.append(n)
    
    if max_n < n:
        max_n = n


is_prime = [True for _ in range(max_n * 2 + 1)]
is_prime[0] = False
is_prime[1] = False

for i in range(2, max_n * 2 + 1):
    if not is_prime[i]:
        continue

    j = 2
    while i * j <= max_n * 2:
        is_prime[i * j] = False
        j += 1


for n in tests:
    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if is_prime[i]:
            cnt += 1

    print(cnt)
