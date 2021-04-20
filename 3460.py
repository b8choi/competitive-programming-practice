t = int(input())
for _ in range(t):
    n = int(input())

    i = 0
    while n > 0:
        r = n % 2
        if r == 1:
            print(i, end=' ')
        n //= 2
        i += 1
    print()
