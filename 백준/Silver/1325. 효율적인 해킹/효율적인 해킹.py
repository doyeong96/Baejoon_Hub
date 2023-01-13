'''

'''
from collections import deque


def bfs(now):
    Q = deque()
    Q.append(now)
    visit = [0] * (n + 1)
    visit[now] = 1
    cnt = 0
    while Q:
        cnt += 1
        N = Q.popleft()
        for i in arr[N]:
            if visit[i] == 0:
                Q.append(i)
                visit[i] = 1
    return cnt


n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)

vis = [[] for _ in range(n + 1)]
MAX = -987654321
for i in range(1, n + 1):
    cnt = bfs(i)
    vis[i] = cnt
    MAX = max(cnt, MAX)

for i in range(1, n + 1):
    if vis[i] == MAX:
        print(i, end=' ')
