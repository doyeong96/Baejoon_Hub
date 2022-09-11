from collections import deque

n = int(input())
nums = deque()
for _ in range(n):
    num = int(input())
    nums.append(num)
# nums = [int(input()) for _ in range(n)]
stack = deque()
dap = deque()
for i in range(1, n + 1):
    stack.append(i)
    dap.append('+')
    while nums[0] == stack[-1]:
        stack.pop()
        dap.append('-')
        nums.popleft()
        if len(stack) == 0:
            break
if stack:
    print('NO')
else:
    for dap in dap:
        print(dap)
