def gcd(a, b):
    if a < b:
        a, b = b, a

    while b > 0:
        r = a % b
        a = b
        b = r

    return a


n = int(input())
gears = [int(x) for x in input().split()]

rot = (1, 1)
for i in range(1, n):
    ratio = (gears[i - 1], gears[i])
    rot = (ratio[0] * rot[0], ratio[1] * rot[1])
    d = gcd(rot[0], rot[1])
    print(f'{rot[0] // d}/{rot[1] // d}')
