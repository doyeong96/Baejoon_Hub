import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
from heapq import heappop, heappush


def dja(r, c):
    q = []
    heappush(q, (0, r, c))
    vis[r][c] = 0
    while q:
        cnt, r, c = heappop(q)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] == 0:
                    if vis[nr][nc] > cnt + 1:
                        vis[nr][nc] = cnt + 1
                        heappush(q, (cnt + 1, nr, nc))
                else:
                    if vis[nr][nc] > cnt:
                        vis[nr][nc] = cnt
                        heappush(q, (cnt, nr, nc))


INF = float('inf')
n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]
vis = [[INF] * n for _ in range(n)]
dja(0, 0)
print(vis[n-1][n-1])
# for v in vis:
#     print(v)
