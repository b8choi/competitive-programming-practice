n = int(input())

points = []
for i in range(n):
    point = [0, 0]
    point[0], point[1] = [int(x) for x in input().split()]
    points.append(point)

points.sort(key=lambda x: x[0])
points.sort(key=lambda x: x[1])

for p in points:
    print(p[0], p[1])
