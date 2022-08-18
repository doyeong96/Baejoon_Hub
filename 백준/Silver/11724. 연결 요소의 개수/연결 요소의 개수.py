def DFS(v):
    visted[v] = 1

    for w in graph[v]:
        if visted[w] == 0:
            DFS(w)
    return visted

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
visted = [0] * (V + 1)

for _ in range(E):
    u, v = map(int, input().split())
    #무향그래프
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, V + 1):
    if visted[i] == 0:
        cnt += 1
        DFS(i)
print(cnt)