# 풀 문제 = 미로

import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline

from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs(sr, sc, scnt, wall):
    Q = deque()
    Q.append((sr, sc, scnt, wall))

    vis[sr][sc][wall] = scnt

    while Q:
        r, c, cnt, wall = Q.popleft()
        if r == n - 1 and c == m - 1:
            return vis[r][c][wall]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m:  # 배열을 벗어나지 않는 범위만
                if arr[nr][nc] == 1 and wall == 0:  # 벽인데 아직 안부셨을때
                    Q.append((nr, nc, cnt + 1, 1))
                    vis[nr][nc][1] = cnt + 1
                elif arr[nr][nc] == 0 and vis[nr][nc][wall] == 0:
                    Q.append((nr, nc, cnt + 1, wall))
                    vis[nr][nc][wall] = cnt + 1

                # 벽이 아닐때

    return -1


n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
vis = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# print(vis)
a = bfs(0, 0, 1, False)
# for v in vis:
#     print(v)
print(a)
