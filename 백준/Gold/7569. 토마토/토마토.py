from collections import deque

dh = [1, -1, 0, 0, 0, 0]
dr = [0, 0, 1, -1, 0, 0]
dc = [0, 0, 0, 0, 1, -1]


Q = deque()

def bfs():
    while Q:
        h, r, c = Q.popleft()
        for d in range(6):
            nh = h + dh[d]
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and arr[nh][nr][nc] == 0 and visit[nh][nr][nc] == 0:
                Q.append((nh,nr,nc))
                visit[nh][nr][nc] = visit[h][r][c] + 1

# 가로 세로
M, N, H = map(int, input().split())
# 배열 입력
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visit = [[[0] * M for _ in range(N)] for _ in range(H)]

for h in range(H):
    for r in range(N):
        for c in range(M):
            if arr[h][r][c] == 1:
                Q.append((h, r, c))
            if arr[h][r][c] == -1:
                visit[h][r][c] = -1

one = len(Q)
bfs()

zcnt = 0
for h in range(H):
    for r in range(N):
        for c in range(M):
            if visit[h][r][c] == 0:
                zcnt += 1
                
DEBUG = zcnt-one

# 전부 익어 있었을 때
if DEBUG == H*N*M:
    day = 0
# 전부 익히지 못했을때
if DEBUG <= H*N*M:
    day= -1
# 전부 다 익게 만들었을때
if DEBUG == 0:
    day = 0
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if day < visit[h][r][c]:
                    day = visit[h][r][c]

print(day)