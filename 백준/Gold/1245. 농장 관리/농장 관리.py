import sys
input = sys.stdin.readline

from collections import deque

dr = [0, 0, -1, 1, 1, 1, -1, -1]
dc = [1, -1, 0, 0, 1, -1, -1, 1]

def dfs(r, c):
    global flag
    vis[r][c] = 1

    for d in range(8):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < m:
            if arr[r][c] < arr[nr][nc]:
                flag = False
            if vis[nr][nc] == 0 and arr[r][c] == arr[nr][nc]:
                dfs(nr, nc)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
vis = [[0] * m for _ in range(n)]

cnt = 0
for r in range(n):
    for c in range(m):
        if arr[r][c] >= 1 and vis[r][c] == 0:
            flag = True
            dfs(r, c)
            if flag:
                cnt += 1
print(cnt)
