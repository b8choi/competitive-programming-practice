w_table = dict()


def w(a, b, c):
    global w_table

    if (a, b, c) in w_table.keys():
        return w_table[(a, b, c)]
    else:
        if a <= 0 or b <= 0 or c <= 0:
            result = 1
        elif a > 20 or b > 20 or c > 20:
            result = w(20, 20, 20)
        elif a < b and b < c:
            result = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            result = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        
        w_table[(a, b, c)] = result
        return result


while True:
    a, b, c = [int(x) for x in input().split()]
    if a == -1 and b == -1 and c == -1:
        break
    else:
        result = w(a, b, c)
        print(f'w({a}, {b}, {c}) = {result}')
