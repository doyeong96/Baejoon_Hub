from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def bfs(x, y, cnt):
    Q = deque()
    Q.append((x, y))
    vis = [[0] * m for _ in range(n)]
    vis[x][y] = 1
    while Q:
        r, c = Q.pop()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and vis[nr][nc] == 0 and arr[nr][nc] == 1:
                Q.append((nr, nc))
                cnt += 1
                vis[nr][nc] = 1
    return cnt


n, m, f = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for _ in range(f):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1

dap = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            dap = max(bfs(i, j, 1), dap)
print(dap)
