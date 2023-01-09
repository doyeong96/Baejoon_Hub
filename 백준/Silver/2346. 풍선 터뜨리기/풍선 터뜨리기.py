from collections import deque

n = int(input())
arr = deque(enumerate(map(int, input().split())))
dap = []
while arr:
    idx, num = arr.popleft()
    dap.append(idx + 1)
    # 양수
    if num > 0:
        arr.rotate(-(num - 1))
    # 음수
    elif num < 0:
        arr.rotate(-num)

print(*dap)
