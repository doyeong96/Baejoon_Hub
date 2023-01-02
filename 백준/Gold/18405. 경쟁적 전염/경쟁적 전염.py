'''
숫자가 빠른 바이러스가 먼저 퍼져 나감
n = 배열 크기
m = 1번부터 바이러스 번호
배열
s 초 뒤에 x,y에 무엇이 있는지
3 3
1 0 2
0 0 0
3 0 0
2 3 2
'''
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
# from heapq import heappop, heappush
from collections import deque


def bfs():
    global vis
    cnt = 0
    while cnt != s:
        for _ in range(len(Q)):
            virus, r, c = Q.popleft()
            vis[r][c] = virus
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < n and vis[nr][nc] == 0:
                    vis[nr][nc] = virus
                    Q.append((virus, nr, nc))
        else:
            cnt += 1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
vis = [[0] * n for _ in range(n)]
Q = deque()

for v in range(1, m + 1):
    for r in range(n):
        for c in range(n):
            if v == arr[r][c]:
                Q.append((v, r, c))

bfs()
print(vis[x-1][y-1])
