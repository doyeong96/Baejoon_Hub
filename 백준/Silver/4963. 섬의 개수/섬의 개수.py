from collections import deque

dr = [0, 0, 1, -1, 1, 1, -1, -1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]


def bfs(r, c):
    global vis
    Q = deque()
    Q.append((r, c))
    vis[r][c] = 1
    while Q:
        r, c = Q.popleft()
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < b and 0 <= nc < a and vis[nr][nc] == 0 and arr[nr][nc] == 1:
                Q.append((nr, nc))
                vis[nr][nc] = 1


while True:
    a, b, = map(int, input().split())
    if a == 0 and b == 0:
        break
    vis = [[0] * a for _ in range(b)]
    arr = [list(map(int, input().split())) for _ in range(b)]
    cnt = 0
    for r in range(b):
        for c in range(a):
            if arr[r][c] == 1 and vis[r][c] == 0:
                bfs(r, c)
                cnt += 1
    print(cnt)
