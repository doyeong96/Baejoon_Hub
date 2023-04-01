import sys



input = sys.stdin.readline

'''
끝나는 조건 
'''
from collections import deque
def bfs():
    vis = [-1] * (n+1)
    Q = deque()
    Q.append(1)
    vis[1] = 0
    while Q:
        a = Q.popleft()
        for b in g[a]:
            if vis[b] == -1:
                vis[b] = vis[a] + 1
                Q.append(b)
    return vis[1:]

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# 1 = 추가
# 2 = 삭제
q = int(input())
for _ in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        g[b].append(c)
        g[c].append(b)
        print(*bfs())
    else:
        g[b].remove(c)
        g[c].remove(b)
        print(*bfs())

# for k in range(n):
#     print(bfs())
