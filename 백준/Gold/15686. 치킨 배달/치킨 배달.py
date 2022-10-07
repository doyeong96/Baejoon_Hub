from itertools import combinations

n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
house, chicken, dap = [], [], 987654321
for i in range(n):
    for j in range(n):
        if MAP[i][j] == 1:
            house.append((i, j))
        if MAP[i][j] == 2:
            chicken.append((i, j))

for C in combinations(chicken, m):
    # 집 기준
    road = 0
    for hr, hc in house:
        minV = 987654321
        for cr, cc in C:
            hap = abs(hr-cr) + abs(hc-cc)
            if minV > hap:
                minV = hap
        road += minV
    if dap > road:
        dap = road

print(dap)