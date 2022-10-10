dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

board = [[0] * 101 for _ in range(101)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    for r in range(x, x + 10):
        for c in range(y, y + 10):
            board[r][c] = 1
dap = 0
for r in range(101):
    for c in range(101):
        if board[r][c] == 1:
            cnt = 0
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if board[nr][nc] == 1:
                    cnt += 1
            if cnt == 2:
                dap += 2
            elif cnt == 3:
                dap += 1
print(dap)
