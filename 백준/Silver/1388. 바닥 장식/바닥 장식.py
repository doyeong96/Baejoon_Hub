from collections import deque


def updown(r, c):
    global cnt
    dr = [1, -1]
    dc = [0, 0]
    Q = deque()
    Q.append((r, c))
    vis[r][c] = 1
    while Q:
        r, c = Q.popleft()
        for d in range(2):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == '|' and vis[nr][nc] == 0:
                Q.append((nr, nc))
                vis[nr][nc] = 1
    cnt += 1


def leftright(r, c):
    global cnt
    dr = [0, 0]
    dc = [1, -1]
    Q = deque()
    Q.append((r, c))
    vis[r][c] = 1
    while Q:
        r, c = Q.popleft()
        for d in range(2):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == '-' and vis[nr][nc] == 0:
                Q.append((nr, nc))
                vis[nr][nc] = 1
    cnt += 1


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
vis = [[0] * m for _ in range(n)]
cnt = 0
for r in range(n):
    for c in range(m):
        if arr[r][c] == '-' and vis[r][c] == 0:
            leftright(r, c)
        elif arr[r][c] == '|' and vis[r][c] == 0:
            updown(r, c)

print(cnt)
