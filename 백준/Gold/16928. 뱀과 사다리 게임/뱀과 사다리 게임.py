from collections import deque


def bfs(start):
    Q = deque()
    Q.append(start)
    # 주사위 굴린 횟수
    cnt = 0
    while Q:
        now = Q.popleft()
        if now == 100:
            return
        for i in range(1, 7):
            nn = now + i
            if nn<101 and vis[nn] == 0:
                if nn in s.keys():
                    nn = s[nn]
                elif nn in l.keys():
                    nn = l[nn]
                if vis[nn] == 0:
                    vis[nn] = vis[now] + 1
                    Q.append(nn)


n, m = map(int, input().split())
s = {}
l = {}
vis = [0] * 101
for _ in range(n):
    a, b = map(int, input().split())
    l[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    s[a] = b

bfs(1)
print(vis[100])