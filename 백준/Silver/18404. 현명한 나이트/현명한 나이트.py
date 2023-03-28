import sys

from collections import deque

dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [-1, 1, -2, 2, -2, 2, -1, 1]


# (X-2,Y-1), (X-2,Y+1), (X-1,Y-2), (X-1,Y+2), (X+1,Y-2), (X+1,Y+2), (X+2,Y-1), (X+2,Y+1)

def bfs(r, c):
    global m
    Q = deque()
    Q.append((r, c))
    vis[r][c] = 1

    flag = True
    while flag:
        r, c= Q.popleft()
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and vis[nr][nc] == 0:
                vis[nr][nc] = vis[r][c] + 1
                Q.append((nr, nc))
                if arr[nr][nc] != 0:
                    m -= 1
                if m == 0:
                    flag = False


n, m = map(int, input().split())
r, c = map(int, input().split())

arr = [[0] * n for _ in range(n)]
vis = [[0] * n for _ in range(n)]

check = []
for i in range(m):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = i + 1
    check.append((a - 1, b - 1))

cnt = [0] * m
bfs(r - 1, c - 1)

for ch in check:
    print(vis[ch[0]][ch[1]]-1, end=' ')
