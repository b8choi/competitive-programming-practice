def validate(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) > 0:
        return False
    return True


n = int(input())

for _ in range(n):
    line = input()
    result = validate(line)
    if result:
        print('YES')
    else:
        print('NO')
