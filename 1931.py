n = int(input())

sessions = [(-1, -1)]
for i in range(n):
    s, e = [int(x) for x in input().split()]
    sessions.append((s, e))

sessions.sort(key=lambda x: x[0])
sessions.sort(key=lambda x: x[1])

cnt = 0
prev_s = -1
prev_e = -1
for i in range(1, n + 1):
    if sessions[i][0] >= prev_e:
        #print(sessions[i][0], sessions[i][1])
        cnt += 1
        prev_s, prev_e = sessions[i]

print(cnt)
