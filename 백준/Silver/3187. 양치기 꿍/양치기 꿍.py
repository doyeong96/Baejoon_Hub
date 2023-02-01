
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
from collections import deque


def bfs(r, c, sheep, wolf):
    global s, w
    # 양, 늑대
    cs, cw = sheep, wolf
    Q = deque()
    Q.append((r, c))
    vis[r][c] = 1
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 범위를 벗어나지 않았고, 울타리가 아니고, 아직 방문하지 않았을 때
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] != '#' and vis[nr][nc] == 0:
                if arr[nr][nc] == 'k':
                    cs += 1
                elif arr[nr][nc] == 'v':
                    cw += 1
                Q.append((nr, nc))
                vis[nr][nc] = 1
    # 양이 많을때
    if cs > cw:
        if cw == 0:
            pass
        else:
            w -= cw
    # 늑대가 많을때
    elif cs <= cw:
        if cs == 0:
            pass
        else:
            s -= cs


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
vis = [[0] * m for _ in range(n)]
# 양, 늑대
s, w = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'k' and vis[i][j] == 0:
            s += 1
        elif arr[i][j] == 'v' and vis[i][j] == 0:
            w += 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'k':
            bfs(i, j, 1, 0)
        elif arr[i][j] == 'v':
            bfs(i, j, 0, 1)

print(s, w)
