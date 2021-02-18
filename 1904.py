n = int(input())

t_0 = 1
t_1 = 1
t_2 = 1

for i in range(2, n + 1):
    t_2 = (t_0 + t_1) % 15746
    t_0 = t_1
    t_1 = t_2

print(t_2)
