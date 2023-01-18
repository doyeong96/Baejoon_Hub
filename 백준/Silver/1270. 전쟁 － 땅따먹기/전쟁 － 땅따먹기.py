for _ in range(int(input())):
    dic = {}
    li = list(map(int, input().split()))
    for i in range(1, li[0] + 1):
        if li[i] in dic:
            dic[li[i]] += 1
        else:
            dic[li[i]] = 1
    maxV = -987654321
    for key, val in dic.items():
        if maxV < val:
            maxV = val
            winner = key
    if maxV > li[0] // 2:
        print(winner)
    else:
        print('SYJKGW')