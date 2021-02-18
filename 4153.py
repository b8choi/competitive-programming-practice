while True:
    sides = [int(x) ** 2 for x in input().split()]
    if (sides == [0, 0, 0]):
        break

    sides.sort()
    if sides[2] == sides[0] + sides[1]:
        print('right')
    else:
        print('wrong')
