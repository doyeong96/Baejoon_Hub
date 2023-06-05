import sys

#sys.stdin = open("0000sample.txt", 'r')
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
'''
l <= 두 나라의 인구 차 <= r => 국경선을 염
각 칸은 (연합인구 / 칸의 개수)

계속해서 bfs를 호출해서 더이상 호출하지 않을때까지 반복시켜야함
'''
from collections import deque


def bfs(r, c):
    global cnt
    Q = deque()
    Q.append((r, c))
    vis[r][c] = 1
    union = [(r, c)]
    people = arr[r][c]
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # l <= 두 나라의 인구 차 <= r
            if 0 <= nr < n and 0 <= nc < n and vis[nr][nc] == 0:  # 범위 내
                mid = abs(arr[nr][nc] - arr[r][c])
                if L <= mid <= R:
                    union.append((nr, nc))
                    Q.append((nr, nc))
                    people += arr[nr][nc]
                    vis[nr][nc] = 1
    return union, people
    # if union:
    #     point = people // len(union)
    #     for ur, uc in union:
    #         arr[ur][uc] = point
    #     return 1
    # else:
    #     return 0


n, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

day = 0
while True:
    flag = True
    vis = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if vis[r][c] == 0:
                union, people = bfs(r, c)

                if len(union) > 1:
                    flag = False
                    point = people // len(union)
                    for ur, uc in union:
                        arr[ur][uc] = point
    if flag:
        break
    day += 1

print(day)
