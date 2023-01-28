dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


# 가희 위치, 현재 진행시간, 먹은 개수
def dfs(r, c, now, eat):
    global maxV
    if now == t:
        maxV = max(maxV, eat)
    else:
        # 가희는 이동할 것이기 때문
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 범위 벗어나지 않게 체크
            if 0 <= nr < n and 0 <= nc < m:
                # 장애물이면 못지나감
                if arr[nr][nc] == '#':
                    continue
                elif arr[nr][nc] == '.':
                    dfs(nr, nc, now + 1, eat)
                elif arr[nr][nc] == 'S':
                    arr[nr][nc] = '.'
                    dfs(nr, nc, now + 1, eat + 1)
                    arr[nr][nc] = 'S'


n, m, t = map(int, input().split())
arr = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'G':
            r, c, = i, j
maxV = 0
arr[r][c] = '.'
dfs(r, c, 0, 0)

print(maxV)