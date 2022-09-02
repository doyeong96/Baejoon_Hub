from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs():
    global cnt
    # visted[i][j] = 1
    while Q:
        # 모두 익어있을 때
        # if len(Q) == (n*m):
        #     return 0
        # 모두 익지 않았을 때
        # else:
        for _ in range(len(Q)):
            r, c = Q.popleft()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                #범위를 벗어나지 않고 옆이 0일때
                if 0 <= nr < n and 0 <= nc < m and tomato[nr][nc] == 0:
                    tomato[nr][nc] = 1
                    Q.append((nr, nc))
        cnt += 1
    return cnt

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
# visted = [[0]*m for _ in range(n)]
Q = deque()
cnt = -1
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            Q.append((i, j))

bfs()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            cnt = -1
            break
    if tomato[i][j] == 0:
        break
print(cnt)