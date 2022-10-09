def clock1(x, y):
    global shop1
    # 좌 하 우 상
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    cnt1 = 0
    d = 0
    for i in range(1, s + 1):
        r, c = x, y
        while arr[r][c] != i:
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < m + 1 and 0 <= nc < n + 1:
                cnt1 += 1
                r, c = nr, nc
                if arr[nr][nc] == i:
                    shop1.append(cnt1)
                    cnt1 = 0
                    d = 0
            else:
                d = (d + 1) % 4


def rclock1(x, y):
    global shop2
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    cnt2 = 0
    d = 0
    for i in range(1, s + 1):
        r, c = x, y
        while arr[r][c] != i:
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < m + 1 and 0 <= nc < n + 1:
                cnt2 += 1
                r, c = nr, nc
                if arr[nr][nc] == i:
                    shop2.append(cnt2)
                    cnt2 = 0
                    d = 0
            else:
                d = (d + 1) % 4


def clock2(x, y):
    global shop1
    # 좌 상 우 하
    dr = [0, -1, 0, 1]
    dc = [-1, 0, 1, 0]
    cnt1 = 0
    d = 0
    for i in range(1, s + 1):
        r, c = x, y
        while arr[r][c] != i:
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < m + 1 and 0 <= nc < n + 1:
                cnt1 += 1
                r, c = nr, nc
                if arr[nr][nc] == i:
                    shop1.append(cnt1)
                    cnt1 = 0
                    d = 0
            else:
                d = (d + 1) % 4


def rclock2(x, y):
    global shop2
    # 우 상 좌 하
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    cnt2 = 0
    d = 0
    for i in range(1, s + 1):
        r, c = x, y
        while arr[r][c] != i:
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < m + 1 and 0 <= nc < n + 1:
                cnt2 += 1
                r, c = nr, nc
                if arr[nr][nc] == i:
                    shop2.append(cnt2)
                    cnt2 = 0
                    d = 0
            else:
                d = (d + 1) % 4


def clock3(x, y):
    global shop1
    # 하 우 상 좌
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    cnt1 = 0
    d = 0
    for i in range(1, s + 1):
        r, c = x, y
        while arr[r][c] != i:
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < m + 1 and 0 <= nc < n + 1:
                cnt1 += 1
                r, c = nr, nc
                if arr[nr][nc] == i:
                    shop1.append(cnt1)
                    cnt1 = 0
                    d = 0
            else:
                d = (d + 1) % 4


def rclock3(x, y):
    global shop2
    # 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    cnt2 = 0
    d = 0
    for i in range(1, s + 1):
        r, c = x, y
        while arr[r][c] != i:
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < m + 1 and 0 <= nc < n + 1:
                cnt2 += 1
                r, c = nr, nc
                if arr[nr][nc] == i:
                    shop2.append(cnt2)
                    cnt2 = 0
                    d = 0
            else:
                d = (d + 1) % 4


def clock4(x, y):
    global shop1
    # 상 좌 하 우
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    cnt1 = 0
    d = 0
    for i in range(1, s + 1):
        r, c = x, y
        while arr[r][c] != i:
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < m + 1 and 0 <= nc < n + 1:
                cnt1 += 1
                r, c = nr, nc
                if arr[nr][nc] == i:
                    shop1.append(cnt1)
                    cnt1 = 0
                    d = 0
            else:
                d = (d + 1) % 4


def rclock4(x, y):
    global shop2
    # 하 좌 상 우
    dr = [1, 0, -1, 0]
    dc = [0, -1, 0, 1]
    cnt2 = 0
    d = 0
    for i in range(1, s + 1):
        r, c = x, y
        while arr[r][c] != i:
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < m + 1 and 0 <= nc < n + 1:
                cnt2 += 1
                r, c = nr, nc
                if arr[nr][nc] == i:
                    shop2.append(cnt2)
                    cnt2 = 0
                    d = 0
            else:
                d = (d + 1) % 4


n, m = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(m + 1)]
# for l in arr:
#     print(l)
# 상점
s = int(input())
for i in range(1, s + 1):
    d, L = map(int, input().split())
    if d == 1:
        arr[0][L] = i
        if i == s + 1:
            arr[0][L] = 'x'
    if d == 2:
        arr[m][L] = i
        if i == s + 1:
            arr[m][L] = 'x'
    if d == 3:
        arr[L][0] = i
        if i == s + 1:
            arr[L][0] = 'x'
    if d == 4:
        arr[L][n] = i
        if i == s + 1:
            arr[L][n] = 'x'

shop1 = []
shop2 = []
dd, dL = map(int, input().split())
if dd == 1:
    clock1(0, dL)
    rclock1(0, dL)
elif dd == 2:
    clock2(m, dL)
    rclock2(m, dL)
elif dd == 3:
    clock3(dL, 0)
    rclock3(dL, 0)
else:
    clock4(dL, n)
    rclock4(dL, n)

dap = 0
for i in range(s):
    dap += min(shop1[i], shop2[i])
print(dap)
