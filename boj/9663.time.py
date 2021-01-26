n = int(input())

cnt = 0

def diag(seq, t):
    arr = seq[:]
    arr.reverse()
    left = t
    right = t

    for i in arr:
        left -= 1
        right += 1
        if left <= 0 and right <= 0:
            break
        if i == left or i == right:
            return False
    return True


def put(seq):
    global cnt

    if len(seq) == n:
        print(seq)
        cnt += 1
    else:
        for i in range(1, n + 1):
            if i not in seq and diag(seq, i):
                put(seq + [i])

put([])

print(cnt)
