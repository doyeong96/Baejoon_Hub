N, M = map(int, input().split())
n = 8
board = [list(map(str, input())) for _ in range(N)]
# 우 하 체크
# dr = [0, 1]
# dc = [1, 0]
change = []

# 8*8 씩 체크
for i in range(N - n + 1):
    for j in range(M - n + 1):
        cntw = 0
        cntb = 0
        for r in range(i, i + n):
            for c in range(j, j + n):
                if (r + c) % 2 == 0:
                    if board[r][c] == 'W':
                        cntb += 1
                    elif board[r][c] == 'B':
                        cntw += 1
                else:
                    if board[r][c] == 'B':
                        cntb += 1
                    elif board[r][c] == 'W':
                        cntw += 1
        change.append(min(cntw, cntb))
print(min(change))