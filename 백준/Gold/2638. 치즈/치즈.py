from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def bfs():
    melt = 0
    visit = [[0] * m for _ in range(n)]
    Q = deque()
    Q.append((0, 0))
    visit[0][0] = 1
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and visit[nr][nc] == 0:
                if arr[nr][nc] >= 1:
                    arr[nr][nc] += 1
                    melt = 1
                else:
                    visit[nr][nc] = 1
                    Q.append((nr, nc))
    return melt

# 세로 가로
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
# visit = [[0] * m for _ in range(n)]

# 소모시간

hour = 0
flag = True
cheese = 0
while flag:
    # bfs 탐방 확인용
    cnt = bfs()
    hour += 1
    for r in range(n):
        for c in range(m):
            if arr[r][c] >= 3:
                arr[r][c] = 0
            elif arr[r][c] == 2:
                arr[r][c] = 1
    if cnt == 0:
        flag = False
print(hour-1)