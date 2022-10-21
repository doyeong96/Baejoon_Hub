from collections import deque

dr = [-1, 0, 1, 0, -1, 1, 1, -1]
dc = [0, 1, 0, -1, 1, 1, -1, -1]


def bfs(r, c):
    Q = deque()
    Q.append((r, c))
    visit[r][c] = 1
    while Q:
        r, c = Q.popleft()
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and visit[nr][nc] == 0 and arr[nr][nc] == 1:
                visit[nr][nc] = 1
                Q.append((nr, nc))


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]

cnt = 0
for r in range(n):
    for c in range(m):
        if visit[r][c] == 0 and arr[r][c] == 1:
            bfs(r, c)
            cnt += 1
print(cnt)
