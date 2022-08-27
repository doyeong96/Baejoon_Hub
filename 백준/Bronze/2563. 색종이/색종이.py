n = 100
board = [[0] * n for _ in range(n)]

for loop in range(int(input())):
    cnt = 0
    r1, c1 = map(int, input().split())
    r2, c2 = r1 + 10, c1 + 10
    # print(r1, c1)
    for r in range(r1, r2):
        for c in range(c1, c2):
            board[r][c] = 1

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt += 1
print(cnt)