dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
from collections import deque


def bfs(r, c):
    global cnt
    Q = deque()
    Q.append((r, c))
    vis[r][c] = 1
    while Q:
        r, c, = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and vis[nr][nc] == 0 and arr[nr][nc] != 'X':
                if arr[nr][nc] == 'O' or arr[nr][nc] == 'P':
                    if arr[nr][nc] == 'P':
                        cnt += 1
                vis[nr][nc] = 1
                Q.append((nr, nc))


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
vis = [[0] * m for _ in range(n)]
cnt = 0
dap = 'TT'
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            bfs(i, j)

if cnt:
    dap = cnt

print(dap)
