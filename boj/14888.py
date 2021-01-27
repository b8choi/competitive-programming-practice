n = int(input())
nums = [int(num) for num in input().split()]
nops = [int(nop) for nop in input().split()]

answer_max = -2000000000
answer_min = 2000000000


def find(result, k, a, s, m, d):
    global nums
    global answer_max
    global answer_min

    if k == n:
        #print(result)
        if answer_max < result:
            answer_max = result
        if answer_min > result:
            answer_min = result
    else:
        for i in range(a):
            find(result + nums[k], k + 1, a - 1, s, m, d)
        for i in range(s):
            find(result - nums[k], k + 1, a, s - 1, m, d)
        for i in range(m):
            find(result * nums[k], k + 1, a, s, m - 1, d)
        for i in range(d):
            find(int(result / nums[k]), k + 1, a, s, m, d - 1)


find(nums[0], 1, nops[0], nops[1], nops[2], nops[3])
print(answer_max)
print(answer_min)
