import sys
input = sys.stdin.readline

from heapq import heappop, heappush

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def dja(s, e):
    q = []
    vis[s][s] = li[s][s]
    # 비용, 좌표
    heappush(q, (li[s][s], 0, 0))
    while q:
        cnt, r, c = heappop(q)
        if r == e and c == e:
            return cnt
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                cost = cnt + li[nr][nc]
                if cost < vis[nr][nc]:
                    vis[nr][nc] = cost
                    heappush(q, (cost, nr, nc))


INF = float('inf')
flag = True
dap = 0
while flag:
    dap += 1
    n = int(input())
    if n == 0:
        break
    li = [list(map(int, input().split())) for _ in range(n)]
    # arr = [list(map(int, input())) for _ in range(n)]
    vis = [[INF] * n for _ in range(n)]
    # print(vis)
    # print(li)
    cost = dja(0, n - 1)
    print(f'Problem {dap}: {cost}')
