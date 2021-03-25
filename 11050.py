def fact(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


n, k = [int(x) for x in input().split()]

res = int(fact(n) / (fact(n - k) * fact(k)))
print(res)
