n = int(input())

members = []
for i in range(n):
    line = input().split()
    age = int(line[0])
    name = line[1]
    members.append((age, name))

members.sort(key=lambda x: x[0])

for age, name in members:
    print(age, name)
