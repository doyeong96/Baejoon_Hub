def dfs(select, check, k):
    # 선택한 치킨집 방문 처리
    global dvisit, dap, road

    if select == m: # and len(check) != 0:
        hap = 0
        minV = 987654321
        # 집 기준 으로 거리 측정
        for hr, hc in house:
            for cr, cc in check:
                hap = abs(hr - cr) + abs(hc - cc)
                if minV > hap:
                    minV = hap

            road += minV
            minV = 987654321
            hap = 0
        if dap > road:
            dap = road
        road = 0
        return

    for i in range(k, len(chicken) - (m - select) + 1):
        dfs(select + 1, check + [chicken[i]], i + 1)
        dfs(select, check, i + 1)

# 최단거리 측정을 위해서 bfs

n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
# house = [[0]*n for _ in range(n)]
chicken = []
house = []
road = 0
for i in range(n):
    for j in range(n):
        # 가정집
        if MAP[i][j] == 1:
            house.append((i, j))
            # house[i][j] = 1
        if MAP[i][j] == 2:
            chicken.append((i, j))

dvisit = [0] * len(chicken)
dap = 987654321
dfs(0, [], 0)
print(dap)