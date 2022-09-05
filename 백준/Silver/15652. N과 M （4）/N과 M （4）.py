def BT(idx):
    if len(dap) == M:
        print(*dap)
        return
    else:
        while idx != N:
            num = nums[idx]
            dap.append(num)
            BT(idx) 
            idx += 1
            dap.pop()
        pass

N,M = map(int, input().split())
nums = [1+i for i in range(N)]
idx=0
dap = []
BT(idx)