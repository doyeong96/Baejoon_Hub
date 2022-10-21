from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def bfs(sr, sc, color):
    global visit
    Q = deque()
    Q.append((r, c, color))
    visit[sr][sc] = 1
    while Q:
        sr, sc, color = Q.popleft()
        for d in range(4):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if 0 <= nr < n and 0 <= nc < n and visit[nr][nc] == 0 and arr[nr][nc] == color:
                visit[nr][nc] = 1
                Q.append((nr, nc, color))
        # for d in range


n = int(input())
arr = [list(input()) for _ in range(n)]
# print(arr)

visit = [[0] * n for _ in range(n)]
cnt = 0
for r in range(n):
    for c in range(n):
        if visit[r][c] == 0:
            bfs(r, c, arr[r][c])
            cnt += 1
print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

visit = [[0] * n for _ in range(n)]
cnt = 0
for r in range(n):
    for c in range(n):
        if visit[r][c] == 0:
            bfs(r, c, arr[r][c])
            cnt += 1
print(cnt)