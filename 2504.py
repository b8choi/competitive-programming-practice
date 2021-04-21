ps = input()

s = []
for p in ps:
    if p == '(':
        s.append('(')
    elif p == '[':
        s.append('[')
    elif p == ')':
        n = 0
        while len(s) > 0 and type(s[-1]) == int:
            n += s.pop()
        if n == 0:
            n = 1

        if len(s) > 0 and s[-1] == '(':
            s.pop()
            s.append(n * 2)
        else:
            print(0)
            exit()
    elif p == ']':
        n = 0
        while len(s) > 0 and type(s[-1]) == int:
            n += s.pop()
        if n == 0:
            n = 1
        if len(s) > 0 and s[-1] == '[':
            s.pop()
            s.append(n * 3)
        else:
            print(0)
            exit()

for v in s:
    if v == '(' or v == '[':
        print(0)
        exit()
print(sum(s))
