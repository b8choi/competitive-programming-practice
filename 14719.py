h, w = [int(x) for x in input().split()]
land = [int(x) for x in input().split()]

water = [0] * w
for i in range(1, w - 1):
    for j in range(h, land[i], -1):
        drain_left = True
        for k in range(0, i):
            if land[k] >= j:
                drain_left = False
                break

        drain_right = True
        for k in range(i + 1, w):
            if land[k] >= j:
                drain_right = False
                break

        if not drain_left and not drain_right:
            water[i] = j
            break

amount = 0
for i in range(w):
    if water[i] > 0:
        amount += water[i] - land[i]

print(amount)
