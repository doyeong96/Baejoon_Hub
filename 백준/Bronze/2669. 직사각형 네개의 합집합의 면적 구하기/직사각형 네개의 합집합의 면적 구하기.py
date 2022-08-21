n = 100
arr = [[0] * n for _ in range(n)]
# for
for _ in range(4):
    r1, c1, r2, c2 = map(int, input().split())

    for r in range(r1, r2):
        for c in range(c1, c2):
            arr[r][c] = 1
#
# for arr in arr:
#     print(*arr)
cnt = 0
for r in range(n):
    for c in range(n):
        if arr[r][c] == 1:
            cnt += 1
print(cnt)