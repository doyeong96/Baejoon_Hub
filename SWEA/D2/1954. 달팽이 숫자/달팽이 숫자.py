t = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for test in range(t):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    r = c = d = 0
    cnt = 1
    arr[r][c] = cnt
    cnt += 1

    while cnt <= n * n:
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
            r = nr
            c = nc
            arr[r][c] = cnt
            cnt += 1
        else:
            d = (d + 1) % 4

    print(f'#{test+1}')
    for i in arr:
        print(*i)