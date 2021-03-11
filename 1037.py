n = int(input())
divisors = [int(x) for x in input().split()]

divisors.sort()

print(divisors[0] * divisors[-1])
