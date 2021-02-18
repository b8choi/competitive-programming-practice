t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = [int(x) for x in input().split()]

    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if d > (r1 + r2) ** 2:
        print('0')
    elif d < (r1 + r2) ** 2:
        if (r1 - r2) ** 2 > d:
            print('0')
        elif (r1 - r2) ** 2 < d:
            print('2')
        else:
            if d == 0:
                print('-1')
            else:
                print('1')
    else:
        print('1')
