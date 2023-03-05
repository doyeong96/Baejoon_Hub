import sys

input = sys.stdin.readline

from collections import deque


def bfs(now):
    Q = deque()
    Q.append(now)
    while Q:
        n= Q.popleft()
        for d in range(8):
            if d >= 6:
                nn = n * way[d]
            else:
                nn = n + way[d]
            if 0 <= nn < 100001 and vis[nn] == 0:
                Q.append(nn)
                vis[nn] = 1
                arr[nn] = arr[n] + 1


a, b, n, m = map(int, input().split())
way = [-1, +1, +a, -a, +b, -b, a, b]
arr = [0] * 100001
vis = [0] * 100001

bfs(n)
print(arr[m])
