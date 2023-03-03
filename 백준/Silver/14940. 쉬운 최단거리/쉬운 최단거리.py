from collections import deque


def bfs(sr, sc):
    Q = deque()
    Q.append((sr, sc))
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<=nr<n and 0<=nc<m and arr[nr][nc] != 0 and vis[nr][nc] == 0:
                Q.append((nr,nc))
                if nr == sr and nc == sc:
                    continue
                else:
                    vis[nr][nc] = vis[r][c] + 1


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
vis = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            break
    if arr[i][j] == 2:
        break
bfs(i, j)
# 갈수있는데 못갔으면 그냥 -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            if vis[i][j] == 0:
                vis[i][j] = -1

for i in range(n):
    for j in range(m):
        print(vis[i][j],end=' ')
    print()