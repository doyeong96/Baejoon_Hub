def BT():
    if len(dap) == M:
        print(*dap)
        return
    else:
        for num in nums:
            dap.append(num)
            BT()
            dap.pop()

N, M = map(int, input().split())
nums = [1+i for i in range(N)]
dap = []
idx = 0
BT()