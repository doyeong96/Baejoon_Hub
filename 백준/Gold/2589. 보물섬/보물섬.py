from collections import deque

# 걍 아무 거나 때려 넣음
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(i, j):
    bomul = 0
    visted = [[0] * c for _ in range(r)]
    q = deque()
    visted[i][j] = 1
    q.append((i, j))
    while q:
        sr1, sc1 = q.popleft()
        for d in range(4):
            nr = sr1 + dr[d]
            nc = sc1 + dc[d]
            # 범위체크 해주고, 움직이는 위치가 땅일때만 가고, 아직 방문 안했고
            if 0 <= nr < r and 0 <= nc < c and zido[nr][nc] == 'L' and visted[nr][nc] == 0:
                visted[nr][nc] = visted[sr1][sc1] + 1
                bomul = max(cnt, visted[nr][nc])
                q.append((nr, nc))
    return bomul - 1

cnt = 0
r, c = map(int, input().split())
zido = [input() for _ in range(r)]
for sr in range(r):
    for sc in range(c):
        # 육지일때만 거리찾으러 가야됨
        if zido[sr][sc] == 'L':
            find = bfs(sr, sc)
            if cnt <= find:
                cnt = find
print(cnt)