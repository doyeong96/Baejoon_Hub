import sys

# sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def bfs(sr, sc, rain):
    global visit
    Q = deque()
    Q.append((sr, sc))
    visit[sr][sc] = 1

    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                # 미방문 상태 이고 강수량 보다 높은 위치
                if visit[nr][nc] == 0 and arr[nr][nc] > rain:
                    Q.append((nr, nc))
                    visit[nr][nc] = 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

maxV = 0
for r in range(n):
    for c in range(n):
        maxV = max(maxV, arr[r][c])

dap = 0
# 잠길수있는 최소부터
for i in range(maxV):
    visit = [[0] * n for _ in range(n)]
    safe = 0
    for r in range(n):
        for c in range(n):
            if visit[r][c] == 0 and arr[r][c] > i:
                bfs(r, c, i)
                safe += 1

    dap = max(dap, safe)

print(dap)
