n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
r = c = 0
d = 0
cnt = 1
check = 0
arr[r][c] = cnt
cnt += 1

while cnt <= n*m:
    nr = r + dr[d]
    nc = c + dc[d]

    if 0 <= nc < m and 0 <= nr < n and arr[nr][nc] == 0:
        r = nr
        c = nc
        arr[r][c] = cnt
        cnt += 1
    else:
        d = (d+1) % 4
        check += 1

print(check)