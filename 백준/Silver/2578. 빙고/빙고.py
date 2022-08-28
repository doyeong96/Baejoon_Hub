def check():
    global Rbingo
    for sr in range(n):
        for sc in range(n):
            if check_board[sr][sc] == 'X':
                for d in range(4):
                    bingo = 0
                    for j in range(5):
                        nr = sr + dr[d] * j
                        nc = sc + dc[d] * j
                        if 0 <= nr < n and 0 <= nc < n and check_board[nr][nc] == 'X':
                            bingo += 1
                        else:
                            break
                    if bingo == 5:
                        Rbingo += 1
    return Rbingo

# 오른쪽 아래 오른쪽아래 왼쪽아래
dr = [0, 1, 1, 1]
dc = [1, 0, 1, -1]

n = 5
board = [list(map(int, input().split())) for _ in range(n)]
check_board = [['0'] * n for _ in range(n)]
# Rbingo = 0
cnt = 0 #사회자 숫자 부르면 증가
# d = 0
for _ in range(n):
    mc = list(map(int, input().split()))
    for i in range(n):
        for r in range(n):
            for c in range(n):
                if board[r][c] == mc[i]:
                    check_board[r][c] = 'X'
                    cnt += 1
                    Rbingo = 0
                    if check() >= 3:
                        print(cnt)
                        exit()