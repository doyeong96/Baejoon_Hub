n = int(input())
board = [[0] * 1001 for _ in range(1001)]
for i in range(1, n + 1):
    x, y, garo, sero = map(int, input().split())
    for r in range(x, x + garo):
        for c in range(y, y + sero):
            board[r][c] = i

for j in range(1, n + 1):
    cnt = 0
    for r in range(1001):
        for c in range(1001):
            if board[r][c] == j:
                cnt += 1

    print(cnt)
