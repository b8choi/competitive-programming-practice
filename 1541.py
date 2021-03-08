exp = input()

group = exp.split('-')

summ = 0
for i, g in enumerate(group):
    nums = [int(x) for x in g.split('+')]
    value = sum(nums)
    if i == 0:
        summ = value
    else:
        summ -= value

print(summ)
