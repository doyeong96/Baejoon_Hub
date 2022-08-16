n = int(input())
mine = [list(input()) for _ in range(n)]
board = [list(input()) for _ in range(n)]
dap = [['.'] * n for _ in range(n)]

# 상 우 하 좌 우상 우하 좌하 좌상
dr = [-1, 0, 1, 0, -1, 1, 1, -1]
dc = [0, 1, 0, -1, 1, 1, -1, -1]
for r in range(n):
    for c in range(n):
        if mine[r][c] == '.' and board[r][c] == 'x': # 안전한 상태 일땐 폭탄 0개
            boom = 0
            for d in range(8): # 8 방향 체크
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr < n and 0 <= nc < n: # nr, nc 가 범위를 벗어나지 않았고
                    if mine[nr][nc] == '*': # 8방향에 폭탄이 있을때 폭탄을 1씩 증가
                        boom += 1
                dap[r][c] = boom

        elif mine[r][c] == '*' and board[r][c] == 'x': # 폭탄을 건드린 상태
            for i in range(n):
                for j in range(n):
                    if mine[i][j] == '*': # 지뢰가 있는 모든 위치에 *표시 해줘야함
                        dap[i][j] = '*'
for j in range(n):
    for k in range(n):
        print(dap[j][k], end='')
    print()