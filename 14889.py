N = 20


n = int(input())

score = []
for i in range(n):
    line = [int(x) for x in input().split()]
    score.append(line)

min_diff = 999999999


def get_score_diff(team):
    global n
    global score

    score_a = 0
    score_b = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if team[i] == 0 and team[j] == 0:
                score_a += score[i][j] + score[j][i]
            elif team[i] == 1 and team[j] == 1:
                score_b += score[i][j] + score[j][i]

    return abs(score_a - score_b)


def match(team, a, b, n):
    global min_diff
    
    if len(team) == n:
        #print(team)
        #print(get_score_diff(team))
        diff = get_score_diff(team)
        if min_diff > diff:
            min_diff = diff
    else:
        if a < n / 2:
            match(team + [0], a + 1, b, n)
        if b < n / 2:
            match(team + [1], a, b + 1, n)


match([0], 1, 0, n)

print(min_diff)
