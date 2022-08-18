def DFS(v):
    visted[v] = 1

    for w in graph[v]:
        if visted[w] == 0:
            DFS(w)
    return visted

V = int(input())
E = int(input())
start = 1
graph = [[] for _ in range(V+1)]

for _ in range(E):
    V_n, E_n = map(int, input().split())
    graph[V_n].append(E_n)
    graph[E_n].append(V_n)

    visted = [0] * (V + 1)

# print(DFS(start))
print(sum(DFS(start))-1)
