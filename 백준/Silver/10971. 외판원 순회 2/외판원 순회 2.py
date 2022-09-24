def find_travel(dep):
    global minV
    S = 0
    if dep == n:
        way = nums + [nums[0]]
        # print(way)
        for i in range(len(way) - 1):
            S += zido[way[i] - 1][way[i + 1] - 1]
            if zido[way[i] - 1][way[i + 1] - 1] == 0:
                return
            if S > minV:
                return
        if minV > S:
            minV = S
    else:
        for i in range(dep, n):
            nums[dep], nums[i] = nums[i], nums[dep]
            find_travel(dep + 1)
            nums[dep], nums[i] = nums[i], nums[dep]


n = int(input())
zido = [list(map(int, input().split())) for _ in range(n)]
nums = [i + 1 for i in range(n)]
minV = 987654321
find_travel(1)
print(minV)
