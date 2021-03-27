def count(size, x, y):
    if size == 1:
        return 0

    half = size / 2
    if y < half:
        if x < half:
            return count(half, x, y)
        else:
            return (half ** 2) + count(half, x - half, y)
    else:
        if x < half:
            return ((half ** 2) * 2) + count(half, x, y - half)
        else:
            return ((half ** 2) * 3) + count(half, x - half, y - half)


n, r, c = [int(x) for x in input().split()]

res = int(count(2 ** n, c, r))
print(res)
