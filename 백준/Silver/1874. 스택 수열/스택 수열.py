n = int(input())
nums = [int(input()) for _ in range(n)]
stack = []
dap = []
for i in range(1, n + 1):
    stack.append(i)
    dap.append('+')
    while nums[0] == stack[-1]:
        stack.pop()
        dap.append('-')
        nums.pop(0)
        if len(stack) == 0:
            break
if stack:
    print('NO')
else:
    for dap in dap:
        print(dap)
