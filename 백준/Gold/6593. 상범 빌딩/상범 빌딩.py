# 풀 문제 = 미로

import sys

input = sys.stdin.readline

from collections import deque

dr = [1, -1, 0, 0, 0, 0]
dc = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]


# 층, 층당 - 세로 가로

def bfs(sh, sr, sc):
    Q = deque()
    Q.append((sh, sr, sc))
    vis[sh][sr][sc] = 1

    while Q:
        z, r, c = Q.popleft()
        # if arr[z][r][c] == 'E':
        #     print(f'Escaped in {vis[z][r][c]-1} minute(s).')
        #     return
        for d in range(6):
            nz = z + dh[d]
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nz < h and 0 <= nr < n and 0 <= nc < m:
                if arr[nz][nr][nc] == '.' and vis[nz][nr][nc] == 0:
                    Q.append((nz, nr, nc))
                    vis[nz][nr][nc] = vis[z][r][c] + 1
                if arr[nz][nr][nc] == 'E':
                    print(f'Escaped in {vis[z][r][c]} minute(s).')
                    return
    print('Trapped!')


while True:
    h, n, m = map(int, input().split())
    if h == 0 and n == 0 and m == 0:
        break

    arr = []
    vis = [[[0] * m for _ in range(n)] for _ in range(h)]

    for i in range(h):
        arr.append([list(input().strip()) for _ in range(n)])
        input().strip()

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 'S':
                    sh, sr, sc = i, j, k
    bfs(sh, sr, sc)