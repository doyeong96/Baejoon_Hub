# 풀 문제 = 미로

import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline

from collections import deque


# 위치, 카운트, 그람을 가지고 있는지, 그람을 획득을 할 것인지
def bfs(r, c, cnt, have, want):
    vis = [[0] * m for _ in range(n)]
    Q = deque()
    Q.append((r, c, cnt))
    vis[r][c] = 1

    while Q:
        r, c, cnt = Q.popleft()

        # 칼 가지고 재시작
        if want and arr[r][c] == 2:
            return bfs(r, c, cnt, True, False)

        if r == n - 1 and c == m - 1:
            return cnt

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and vis[nr][nc] == 0:
                # 그람을 가진 상태
                if have:
                    Q.append((nr, nc, cnt + 1))
                    vis[nr][nc] = 1
                # 그람을 가지지 못한 상태
                else:
                    if arr[nr][nc] == 1:
                        continue
                    Q.append((nr, nc, cnt + 1))
                    vis[nr][nc] = 1
    return k + 1


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 그람 없이 가는 bfs
a = bfs(0, 0, 0, False, False)
# 그람 가지고 가는 bfs
b = bfs(0, 0, 0, False, True)

minv = min(a, b)
if minv > k:
    print('Fail')
else:
    print(minv)
