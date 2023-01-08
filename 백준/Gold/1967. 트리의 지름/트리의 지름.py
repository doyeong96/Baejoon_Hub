import sys;
input = sys.stdin.readline

from collections import deque

def BFS(node, LEN):
    global n, res
    visited = [0] * (n + 1)
    Q = deque()
    visited[node] = 1
    Q.append((node, LEN))
    while Q:
        now, now_dist = Q.popleft()
        res.append((now, now_dist))
        for node, dist in graph[now]:
            if visited[node] == 0:
                visited[node] = 1
                Q.append((node, now_dist + dist))


n = int(input())
graph = [[] for _ in range(n + 2)]

for _ in range(n - 1):
    p, c, L = map(int, input().split())
    graph[p].append([c, L])
    graph[c].append([p, L])

res = []
BFS(1, 0)
find = max(res, key=lambda x: x[1])
start_node = find[0]
res = []
BFS(start_node, 0)
find = max(res, key=lambda x: x[1])
print(find[1])