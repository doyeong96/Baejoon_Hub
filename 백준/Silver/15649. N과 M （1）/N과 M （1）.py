def BT(makenum):
    if M == len(makenum):
        print(*makenum)
        return
    else:
        for num in nums:
            if num in makenum:
                continue
            else:
                makenum.append(num)
                BT(makenum)
                makenum.pop()

N, M = map(int, input().split())
nums = [1 + i for i in range(N)]
makenum = []
# dap = []
# # idx = 0
BT(makenum)