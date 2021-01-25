n = int(input())

cnt = 0

numbers = [int(x) for x in input().split()]
for num in numbers:
    if num == 1:
        continue
    else:
        divided = False
        for i in range(2, num):
            if num % i == 0:
                divided = True
                break

        if not divided:
            cnt += 1

print(cnt)
