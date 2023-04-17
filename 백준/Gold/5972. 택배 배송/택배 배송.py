from heapq import heappop, heappush


def djk(start):
    global cnt
    Q = []
    heappush(Q, (0, 1))
    while Q:
        cost, now = heappop(Q)
        if now == n:
            return vis[now]
        if vis[now] < cost:
            continue
        for cow, node in arr[now]:
            if vis[node] > cost + cow:
                vis[node] = cow + cost
                heappush(Q, (cow + cost, node))


n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
vis = [987654321] * (n + 1)

for _ in range(m):
    a, b, c, = map(int, input().split())
    arr[a].append((c, b))
    arr[b].append((c, a))
print(djk(1))
