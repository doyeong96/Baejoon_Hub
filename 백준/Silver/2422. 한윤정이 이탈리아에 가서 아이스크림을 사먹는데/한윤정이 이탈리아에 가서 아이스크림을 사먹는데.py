n, m = map(int, input().split())
no = [[[0] for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    no[a][b] = 1
    no[b][a] = 1

cnt = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            if no[i][j] != 1 and no[i][k] != 1 and no[j][k] != 1:
                cnt += 1
print(cnt)
