import sys

input = sys.stdin.readline
'''
(r, c)라면, 
(r-2, c-1)
(r-2, c+1)
(r, c-2)
(r, c+2)
(r+2, c-1)
(r+2, c+1)로 이동할 수 있다.
'''
from collections import deque

dr = [-2, -2, 0, 0, +2, +2]
dc = [-1, +1, -2, +2, -1, +1]


def bfs(r, c):
    Q = deque()
    Q.append((r, c))
    arr[r][c] = 1

    while Q:
        r, c = Q.popleft()
        for d in range(6):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
                Q.append((nr, nc))
                arr[nr][nc] = arr[r][c] + 1


n = int(input())
r1, c1, r2, c2 = map(int, input().split())
arr = [[0] * n for _ in range(n)]
vis = [[0] * n for _ in range(n)]
bfs(r1, c1)

if arr[r2][c2] == 0:
    print(-1)
else:
    print(arr[r2][c2] - 1)