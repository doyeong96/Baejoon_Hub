dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
from collections import deque


# 1, 2
def bfs(v):
    global dap
    vis[v] = 1
    Q = deque()
    Q.append((v, 0))

    while Q:
        now, cnt = Q.popleft()
        if now == b:
            dap = min(dap, cnt)
        for nxt in arr[now]:
            if vis[nxt] == 0:
                vis[nxt] = 1
                Q.append((nxt, cnt + 1))


MAX = 987654321
a, b = map(int, input().split())
n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
dap = MAX
for _ in range(m):
    c, d = map(int, input().split())
    arr[c].append(d)
    arr[d].append(c)
vis = [0] * (n + 1)

bfs(a)
if dap == MAX:
    dap = -1
print(dap)
