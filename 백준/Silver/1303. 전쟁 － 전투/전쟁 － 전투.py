'''
5 5
WBWWW
WWWWW
BBBBB
BBBWW
WWWWW
'''
from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def bfsw(r, c):
    cnt = 1
    Q = deque()
    Q.append((r, c))
    vw[r][c] = 1
    arr[r][c] = 1
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < m and 0 <= nc < n and arr[nr][nc] == 'W' and vw[nr][nc] == 0:
                Q.append((nr, nc))
                arr[nr][nc] = 1
                vw[nr][nc] = 1
                cnt += 1
    cnt *= cnt
    return cnt


def bfsb(r, c):
    cnt = 1
    Q = deque()
    Q.append((r, c))
    vb[r][c] = 1
    arr[r][c] = 1
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < m and 0 <= nc < n and arr[nr][nc] == 'B' and vb[nr][nc] == 0:
                Q.append((nr, nc))
                arr[nr][nc] = 1
                vb[nr][nc] = 1
                cnt += 1
    cnt *= cnt
    return cnt


n, m = map(int, input().split())
arr = [list(input()) for _ in range(m)]
vw = [[0] * n for _ in range(m)]
vb = [[0] * n for _ in range(m)]
B = W = 0
for r in range(m):
    for c in range(n):
        if arr[r][c] == 'W':
            W += bfsw(r, c)
            pass
        elif arr[r][c] == 'B':
            B += bfsb(r, c)
            pass

print(W, B)
'''
가로 n
세로 m
'''