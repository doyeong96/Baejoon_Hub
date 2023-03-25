import sys
input = sys.stdin.readline

from collections import deque

'''

뱀이 사과를 먹는 경우 => 꼬리가 증가, 꼬리 위치 유지
뱀이 사과를 먹지 못하는 경우 => 꼬리 증가 없음, 꼬리 위치 이동
종료 조건

벽에 닿을때
머리의 다음 좌표가 이미 뱀 좌표 안에 있을때
next = 1,0 snake = [0,0 1,0] => 종료

방향 전환
'''

# row, colum
L = [0, 1]
R = [0, -1]
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


# 방향전환 함수
def change(dir, d):
    if dir == 'L':
        if d == 0:
            d = 3
        elif d == 3:
            d = 2
        elif d == 2:
            d = 1
        else:
            d = 0
    else:
        if d == 0:
            d = 1
        elif d == 1:
            d = 2
        elif d == 2:
            d = 3
        else:
            d = 0
    return d


# 이동 함수
def move(sr, sc, d):
    global cnt, time
    while True:
        nr = sr + dr[d]
        nc = sc + dc[d]
        if 0 <= nr < n and 0 <= nc < n:
            if [nr, nc] not in snake:
            # 사과가 있으면
                if arr[nr][nc] == 1:
                    snake.append([nr, nc])
                    arr[nr][nc] = 0
                else:
                    snake.popleft()
                    snake.append([nr, nc])
                sr = nr
                sc = nc
                cnt += 1
                if time:
                    if cnt == int(time[0][0]):
                        dummy = time.pop(0)
                        d = change(dummy[1], d)
            else:
                return cnt + 1
        else:
            return cnt + 1


# 보드
n = int(input())
arr = [[0] * n for _ in range(n)]

# 사과
m = int(input())
for _ in range(m):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

# 이동
k = int(input())

# 시간, 방향
time = [tuple(input().split()) for _ in range(k)]
# print(time[0][0])

snake = deque()
snake.append([0, 0])
cnt = 0
print(move(0, 0, 0))
