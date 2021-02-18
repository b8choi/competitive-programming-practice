import sys


n = int(input())

seq = []
for i in range(n):
    line = sys.stdin.readline().strip()
    seq.append(int(line))


tot = 0
cnt_neg = [0] * 4001
cnt_pos = [0] * 4001

for num in seq:
    tot += num

    if num < 0:
        cnt_neg[-num] += 1
    else:
        cnt_pos[num] += 1


seq = []
freq = []
for i in range(500001):
    freq.append([])

for i in range(4000, 0, -1):
    if cnt_neg[i] > 0:
        series = [-i] * cnt_neg[i]
        seq.extend(series)
        freq[cnt_neg[i]].append(-i)

for i in range(0, 4001):
    if cnt_pos[i] > 0:
        series = [i] * cnt_pos[i]
        seq.extend(series)
        freq[cnt_pos[i]].append(i)


if n % 2 == 0:
    med = (seq[n / 2] + seq[(n / 2) - 1]) / 2
else:
    med = seq[n // 2]

for i in range(500000, 0, -1):
    if freq[i]:
        most_freq = freq[i][0]
        if len(freq[i]) > 1:
            most_freq = freq[i][1]
        break


print(round(tot / n))
print(med)
print(most_freq)
print(seq[-1] - seq[0])
