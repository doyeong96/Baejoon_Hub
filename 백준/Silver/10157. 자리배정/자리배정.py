# 하 우 상 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# # 상 우 하  좌
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]

n, m = map(int, input().split())
t = int(input())

if n * m < t:
    print(0)
    exit()

arr = [[0] * n for _ in range(m)]
r, c = 0, 0
cnt = 1
arr[r][c] = cnt
cnt += 1
d = 0

while cnt != n * m + 1:
    if arr[r][c] == t:
        break
    nr = r + dr[d]
    nc = c + dc[d]
    if 0 <= nr < m and 0 <= nc < n and arr[nr][nc] == 0:
        arr[nr][nc] = cnt
        cnt += 1
        r = nr
        c = nc
    else:
        d = (d + 1) % 4

print(c + 1, r + 1)
