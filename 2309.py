heights = []
for _ in range(9):
    h = int(input())
    heights.append(h)
heights.sort()

total = sum(heights)
a = b = -1
for i in range(8):
    for j in range(i + 1, 9):
        if total - heights[i] - heights[j] == 100:
            a = i
            b = j
            break
    if a >= 0 or b >= 0:
        break

for h in heights:
    if h != heights[a] and h != heights[b]:
        print(h)
