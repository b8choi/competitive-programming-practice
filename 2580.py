N = 9

section = [
    [0, 0, 0, 1, 1, 1, 2, 2, 2],
    [0, 0, 0, 1, 1, 1, 2, 2, 2],
    [0, 0, 0, 1, 1, 1, 2, 2, 2],
    [3, 3, 3, 4, 4, 4, 5, 5, 5],
    [3, 3, 3, 4, 4, 4, 5, 5, 5],
    [3, 3, 3, 4, 4, 4, 5, 5, 5],
    [6, 6, 6, 7, 7, 7, 8, 8, 8],
    [6, 6, 6, 7, 7, 7, 8, 8, 8],
    [6, 6, 6, 7, 7, 7, 8, 8, 8]
]


chk_row = [[0 for j in range(N + 1)] for i in range(9)]
chk_col = [[0 for j in range(N + 1)] for i in range(9)]
chk_sec = [[0 for j in range(N + 1)] for i in range(9)]


board = []
for _ in range(N):
    line = [int(x) for x in input().split()]
    board.append(line)

for i in range(N):
    for j in range(N):
        chk_row[i][board[i][j]] = 1
        chk_col[j][board[i][j]] = 1
        chk_sec[section[i][j]][board[i][j]] = 1


def print_board():
    global board

    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()


def fill(row, col):
    global board
    
    if row == N:
        print_board()
        exit()
    else:
        nrow = row
        ncol = col + 1
        if ncol == N:
            nrow += 1
            ncol = 0

        if board[row][col] == 0:
            for i in range(1, N + 1):
                if not chk_row[row][i] and not chk_col[col][i] and not chk_sec[section[row][col]][i]:
                    board[row][col] = i
                    chk_row[row][i] = 1
                    chk_col[col][i] = 1
                    chk_sec[section[row][col]][i] = 1

                    fill(nrow, ncol)

                    board[row][col] = 0
                    chk_row[row][i] = 0
                    chk_col[col][i] = 0
                    chk_sec[section[row][col]][i] = 0
        else:
            fill(nrow, ncol)


fill(0, 0)
