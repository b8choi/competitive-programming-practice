a, b = [int(x) for x in input().split()]
if a > b:
    a, b = b, a

gcd = 1
for i in range(a, 1, -1):
    if a % i == 0 and b % i == 0:
        gcd = i
        break

lcm = a * b
for i in range(1, a):
    if (b * i) % a == 0:
        lcm = b * i
        break

print(gcd)
print(lcm)
