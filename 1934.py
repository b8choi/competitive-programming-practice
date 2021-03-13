def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


n = int(input())

for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a < b:
        a, b = b, a

    res = int((a * b) / gcd(a, b))
    print(res)
