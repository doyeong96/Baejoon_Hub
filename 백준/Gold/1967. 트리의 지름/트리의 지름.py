import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def DFS(node_num, LEN):
    # 그래프에 노드번호, 길이 순으로 저장돼 있음
    for node, Len in graph[node_num]:
        if res[node] == 0:
            res[node] = Len + LEN
            DFS(node, LEN + Len)


n = int(input())
graph = [[] for _ in range(n + 2)]
if n == 1:
    print(0)
    exit()
for _ in range(n - 1):
    p, c, L = map(int, input().split())
    graph[p].append([c, L])
    graph[c].append([p, L])

# 루트 노드 기준으로 최장길이 노드를 찾는 첫번째 dfs 저장 배열
res = [0] * (n + 2)
res[1] = 1
DFS(1, 0)
# start_node = 루트에서 가장 길이가 먼 노드의 위치
start_node = res.index(max(res))

# start_node 기준으로 또 다시 거리를 찾기 위함
# 배열 초기화
res = [0] * (n + 2)
res[start_node] = 1
DFS(start_node, 0)

print(max(res))
