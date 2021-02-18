n = int(input())

arr = []
for i in range(n):
    m = int(input())
    arr.append(m)

#print(arr)

for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

for i in range(n):
    print(arr[i])
