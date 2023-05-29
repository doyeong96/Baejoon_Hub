import sys

# sys.stdin = open("0000sample.txt", 'r')
input = sys.stdin.readline

from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs():
    Q = deque()
    # r,c,cnt,k,wall(0,1)
    # 좌표, 이동개수, 부순개수, 벽을 다 부쉈는지 확인
    Q.append((0, 0, 1, 0, 0))
    vis[0][0][0] = 1

    while Q:
        r, c, cnt, broke, wall = Q.popleft()
        if r == n - 1 and c == m - 1:
            return vis[r][c][broke]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m:  # 범위 안에서만
                if arr[nr][nc] == 1 and wall == 0:  # 벽을 만난 상태일때
                    # 아직 벽을 부술 수 있을때
                    if broke + 1 == k:
                        Q.append((nr, nc, cnt + 1, broke + 1, 1))
                        vis[nr][nc][broke] = cnt + 1
                    elif broke + 1 < k and vis[nr][nc][broke] == 0:
                        Q.append((nr, nc, cnt + 1, broke + 1, wall))
                        vis[nr][nc][broke] = cnt + 1
                elif arr[nr][nc] == 0 and vis[nr][nc][broke] == 0:  # 벽이 아닐때
                    Q.append((nr, nc, cnt + 1, broke, wall))
                    vis[nr][nc][broke] = cnt + 1
    return -1


# 배열 크기, 부술수 있는 벽
n, m, k = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
vis = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]

print(bfs())
# print(a)
