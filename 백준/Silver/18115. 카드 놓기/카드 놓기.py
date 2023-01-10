from collections import deque

n = int(input())
arr = list(map(int, input().split()))
card = deque(range(1, n + 1))
dap = deque()

for i in reversed(arr):
    if i == 1:
        dap.appendleft(card.popleft())
    elif i == 2:
        dap.insert(1, card.popleft())
    elif i == 3:
        dap.append(card.popleft())
print(*dap)
