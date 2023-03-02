'''
현 위치 = 왼쪽 맨아래 (n-1,0)
집 위치 = 오른쪽 맨 위 (0,m-1)
T = 못가는곳
'''

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def dfs(r, c, cnt):
    global glocnt
    st = [(r, c, cnt)]
    vis[r][c] = 1
    if cnt == t:
        if r == 0 and c == m-1:
            glocnt += 1
    else:
        r, c, cnt = st.pop()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and vis[nr][nc] == 0 and arr[nr][nc] != 'T':
                vis[nr][nc] = 1
                dfs(nr, nc, cnt + 1)
                vis[nr][nc] = 0

n, m, t = map(int, input().split())
arr = [list(input()) for _ in range(n)]
vis = [[0] * m for _ in range(n)]
glocnt = 0
dfs(n - 1, 0, 1)
print(glocnt)