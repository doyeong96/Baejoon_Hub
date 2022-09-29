from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(x, y):
    global visited
    Q = deque()
    Q.append((x, y))
    visited[x][y] = 1

    while Q:
        r, c = Q.popleft()
        arr[r][c] = 0
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 1:
                    arr[nr][nc] = 0
                    Q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
bfs(0, 0)
print(visited[n-1][m-1])