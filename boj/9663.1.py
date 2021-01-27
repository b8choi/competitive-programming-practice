def put(k):
    global cnt

    if k > n:
        '''
        print(seq)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if ban[i][j]:
                    print('1', end=' ')
                else:
                    print('0', end=' ')
            print()
        print()
        '''
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ban[k][i] == 0:
                left = right = i
                for j in range(k + 1, n + 1):
                    ban[j][i] += 1

                    left -= 1
                    right += 1
                    if left > 0:
                        ban[j][left] += 1
                    if right <= n:
                        ban[j][right] += 1

                put(k + 1)

                left = right = i
                for j in range(k + 1, n + 1):
                    ban[j][i] -= 1
                    
                    left -= 1
                    right += 1
                    if left > 0:
                        ban[j][left] -= 1
                    if right <= n:
                        ban[j][right] -= 1


n = int(input())

cnt = 0

ban = []
for i in range(n + 1):
    row = []
    for j in range(n + 1):
        row.append(0)
    ban.append(row)

put(1)

print(cnt)
