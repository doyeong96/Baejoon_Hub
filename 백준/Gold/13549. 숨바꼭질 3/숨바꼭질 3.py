import sys
input = sys.stdin.readline

from heapq import heappop, heappush

MAX = 100001
INF = 987654321


def bfs(now, target):
    li = []
    heappush(li, [0, now])
    vis[now] = 1
    while li:
        cnt, now = heappop(li)
        for d in range(3):
            # 순간이동
            if d == 0:
                nn = now * di[d]
                # 범위를 벗어나지 않게
                if 0 <= nn < MAX:
                    if check[nn] > cnt:
                        heappush(li, [cnt, nn])
                        check[nn] = cnt
                        vis[nn] = 1
            # 순간이동 아닐때
            else:
                nn = now + di[d]
                if 0 <= nn < MAX:
                    if check[nn] > cnt + 1:
                        heappush(li, [cnt + 1, nn])
                        check[nn] = cnt + 1
                        vis[nn] = 1


n, m = map(int, input().split())
if n == m:
    print(0)
    exit()
di = [2, -1, +1]
vis = [0] * MAX
check = [INF] * MAX
bfs(n, m)
print(check[m])
