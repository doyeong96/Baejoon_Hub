from collections import deque


def bfs():
    # 시작 위치, 현재 위치
    Q = deque()
    Q.append((0, 0))
    vis[0][0] = 1
    for i in range(n):
        for j in range(len(Q)):
            r, c = Q.popleft()
            for nr, nc in [(r, c - 1), (r, c + 1), (not r, c + m)]:
                if nc >= n:
                    return 1
                if nc > i and vis[nr][nc] == 0 and arr[nr][nc] == 1:
                    Q.append((nr, nc))
                    vis[nr][nc] = 1
    return 0


n, m = map(int, input().split())
dir = [-1, 1, m]
arr = [list(map(int, input())) for _ in range(2)]
vis = [[0] * n for _ in range(2)]

print(bfs())

# print(li1, li2)
