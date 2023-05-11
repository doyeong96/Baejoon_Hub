# 풀 문제 = 미로

import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline
'''

1에서 N까지 번호가 매겨진 N개의 목장에서 각각 한 마리의 소가 있으며, 이들은 소가 있는 목장에서 열리는 큰 소 파티에 참석하기로 결정했습니다. 
이 파티는 X번 목장에서 열립니다 (1 <= X <= N). M (1 <= M <= 100,000)개의 양방향 도로가 각 목장을 연결하며, 어떤 두 목장 사이에든 도로를 통해 이동할 수 있습니다. 
도로 i를 통과하는 데는 Ti (1 <= Ti <= 100) 단위의 시간이 걸립니다. 하나 이상의 쌍이 동일한 두 목장을 직접 연결할 수 있습니다.

소들이 목장 X에서 파티에 참석했을 때 모든 소가 자신의 파티 선물을 놓고 온 것을 깨달았습니다.
그래서 소들은 파티를 중단하고 모든 소가 자신의 목장으로 가서 선물을 가져오도록 결정했습니다. 
소들은 모두 자신의 목장에서 목장 X까지의 최적 경로를 따라 이동하고, 선물을 가져온 후 최적 경로를 따라 다시 파티로 돌아옵니다. 
모든 소가 자신의 선물을 가져오고 파티 장소로 돌아오는 데 필요한 최소한의 시간은 얼마입니까?

Line 1: Three space-separated integers, respectively: N, M, and X
2부터 M+1까지의 줄: i+1번째 줄은 세 개의 공백으로 구분된 정수로 도로 i를 설명합니다. 
각각 Ai, Bi 및 Ti입니다. 설명된 도로는 Ai와 Bi를 연결하며, 이를 통과하는 데 Ti 시간 단위가 소요됩니다.

n개의 목장
m개의 연결
시작 목장
'''

from heapq import heappop, heappush


def dja(start):
    vis = [INF] * (n + 1)
    Q = []
    heappush(Q, (0, start))
    vis[start] = 0

    while Q:
        cnt, node = heappop(Q)
        if vis[node] < cnt:  # 현재 위치의 비용보다 더 큰 비용을 가지면 그냥 중단
            continue
        for n_node, price in g[node]:
            cost = cnt + price
            if vis[n_node] > cost:
                heappush(Q, (cost, n_node))
                vis[n_node] = cost
    return vis


INF = float('inf')
n, m, x = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    # 다음 노드와 비용
    g[a].append((b, c))
    g[b].append((a, c))
# print(g)

res = dja(x)
cnt = -INF

for i in range(1, n + 1):
    cnt = max(res[i],cnt)
print(cnt*2)
#     if i != x:
#         res = dja(i)
    # cnt = max(cnt, res[x+1])
    # print(res)
