n = int(input())

i = 666
j = 0
while True:
    cnt = 0
    tmp = i
    while tmp > 0:
        if tmp % 10 == 6:
            cnt += 1
            if cnt >= 3:
                j += 1
                break
        else:
            cnt = 0
        tmp = int(tmp / 10)

    if j == n:
        break

    i += 1

print(i)
