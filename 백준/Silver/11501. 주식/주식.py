for _ in range(int(input())):
    n = int(input())
    m = 0
    li = list(map(int, input().split()))
    maxV = li[-1]
    for i in range(n - 2, -1, -1):  # 두번째 뒤 부터 보고 옴
        if maxV < li[i]:
            maxV = li[i]
        else:
            m += maxV - li[i]
    print(m)