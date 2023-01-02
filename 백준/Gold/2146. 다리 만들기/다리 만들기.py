from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


# 섬 바꾸는 함수
def bfs(r, c, change):
    Q = deque()
    Q.append((r, c))
    while Q:
        r, c = Q.popleft()
        arr[r][c] = cnt
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 1:
                arr[nr][nc] = change
                Q.append((nr, nc))


# 다리 놓는 함수
def bfs2(r, c, num, cnt):
    global bridge, minV
    visit = [[0] * n for _ in range(n)]
    Q = deque()
    # 좌표, 섬번호, 카운팅
    Q.append((r, c, num, cnt))
    while Q:
        r, c, num, cnt = Q.popleft()
        if cnt > minV:
            continue
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and visit[nr][nc] == 0:
                # 다음으로 이동하려는 위치가 시작섬과 다른 섬이면
                if arr[nr][nc] != 0 and arr[nr][nc] != num:
                    # bridge.append(cnt)
                    minV = min(minV, cnt)
                # 0이면 바다니까 일단 이동은 해야됨
                if arr[nr][nc] == 0:
                    Q.append((nr, nc, num, cnt + 1))
                visit[nr][nc] = 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
minV = 987654321

# 섬 번호 변경
cnt = 2
for r in range(n):
    for c in range(n):
        if arr[r][c] == 1:
            bfs(r, c, cnt)
            cnt += 1

# for arr in arr:
#     print(*arr)

bridge = []
# 다리 잇는 위치
for r in range(n):
    for c in range(n):
        if arr[r][c] != 0:
            # 좌표 r,c,섬번호,다리 길이 후보
            bfs2(r, c, arr[r][c], 0)
# print(Q2)
# print(bridge)
# print(min(bridge))
print(minV)