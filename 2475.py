digits = [int(x) for x in input().split()]

checksum = 0
for d in digits:
    checksum += d * d

print(checksum % 10)
