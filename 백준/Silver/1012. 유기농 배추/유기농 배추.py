from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def bfs(sr, sc):
    Q = deque()
    Q.append((sr, sc))
    arr[sr][sc] = 0

    while Q:
        sr, sc = Q.popleft()
        for d in range(4):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if 0 <= nr < m and 0 <= nc < n:
                if arr[nr][nc] == 1:
                    Q.append((nr, nc))
                    arr[nr][nc] = 0


for test in range(int(input())):
    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1
    cnt = 0
    for r in range(m):
        for c in range(n):
            if arr[r][c] == 1:
                bfs(r, c)
                cnt += 1

    print(cnt)
