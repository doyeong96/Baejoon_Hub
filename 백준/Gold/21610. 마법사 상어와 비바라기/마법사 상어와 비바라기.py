import sys

# sys.stdin = open("0000sample.txt", 'r')
input = sys.stdin.readline
from collections import deque

# 8방향
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

# 대각선 방향


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 구름이 사라진 위치에 또 다시 구름이 생기지 않게 체크
# 초기구름
cloud = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])


# while cloud:
#     print(cloud.popleft())

def go(move, lenth):
    global cloud

    for _ in range(len(cloud)):
        r, c = cloud.popleft()
        nr = (r + dr[move] * lenth) % n
        nc = (c + dc[move] * lenth) % n
        # print(nr, nc, arr[nr][nc])
        arr[nr][nc] += 1
        cloud.append((nr, nc))

    # 물 빨아들임
    while cloud:
        r, c = cloud.popleft()
        vis[r][c] = 0
        for d in range(1, 8, 2):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] != 0:
                    arr[r][c] += 1
    make()


def make():
    for r in range(n):
        for c in range(n):
            if arr[r][c] >= 2 and vis[r][c] == -1:
                cloud.append((r, c))
                arr[r][c] -= 2


for _ in range(m):
    vis = [[-1] * n for _ in range(n)]
    # 방향, 거리
    a, b = map(int, input().split())
    # 구름이 이동하는 함수 호출
    go(a - 1, b)

# for a in arr:
#     print(*a)

s = 0
for r in range(n):
    for c in range(n):
        s += arr[r][c]
print(s)
