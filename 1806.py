n, s = [int(x) for x in input().split()]
seq = [int(x) for x in input().split()]

answer = 200000

front = 0
rear = 0
summ = seq[0]
while True:
    #print(front, rear, summ)
    if summ >= s and answer > rear - front + 1:
        answer = rear - front + 1

    if summ <= s:
        if rear < n - 1:
            rear += 1
            summ += seq[rear]
        else:
            break
    else:
        summ -= seq[front]
        front += 1

if answer == 200000:
    print(0)
else:
    print(answer)
