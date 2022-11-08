from collections import deque

n,k = map(int,input().split())
Q = deque(range(1, n+1))
dap = []
while Q:
    for _ in range(k-1):
        Q.append(Q.popleft())
    yosep = str(Q.popleft())
    dap.append(yosep)
print('<' + ', '.join(dap) + '>')