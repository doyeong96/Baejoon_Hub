import sys

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def dfs(sr, sc, scnt):
    global maxV, vis
    st = [(sr, sc, scnt)]
    vis[(ord(arr[sr][sc]) - 65)] = 1
    while st:
        r, c, cnt = st.pop()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and vis[(ord(arr[nr][nc]) - 65)] == 0:
                vis[(ord(arr[nr][nc]) - 65)] = 1
                dfs(nr, nc, cnt + 1)
                vis[(ord(arr[nr][nc]) - 65)] = 0
        else:
            maxV = max(maxV, cnt)


n, m = map(int, input().split())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]
maxV = -987654321
vis = [0] * 26
dfs(0, 0, 1)
print(maxV)

# print(ord('A')-ord('Z'))
# print(ord('Z'))
