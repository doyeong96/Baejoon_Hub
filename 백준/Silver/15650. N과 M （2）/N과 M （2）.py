def BT(idx):
    # global idx
    if len(dap) == M:
        print(*dap)
        return
    else:
        while idx != N:
            num = nums[idx]
            dap.append(num)
            BT(idx+1)
            idx+=1
            dap.pop()

N,M = map(int, input().split())
nums = [1+i for i in range(N)]
idx = 0
dap = []
BT(idx)