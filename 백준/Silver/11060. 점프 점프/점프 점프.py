from collections import deque


def bfs(pos, r):
    Q = deque()
    Q.append((pos, li[r]))
    while Q:
        now, dir = Q.popleft()
        for d in range(1, dir + 1):
            if now + d >= n or vis[now + d] != 0:
                continue
            vis[now + d] = vis[now] + 1
            Q.append((now + d, li[now + d]))


n = int(input())
li = list(map(int, input().split()))

if n == 1:
    print(0)
    exit()
vis = [0] * n
cnt = 0
bfs(0, 0)
if vis[-1] == 0:
    print(-1)
else:
    print(vis[-1])
# bfs(0, 0)
