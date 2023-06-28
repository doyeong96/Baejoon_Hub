# https://www.acmicpc.net/problem/2468
import sys

# sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

INF = 987654321


def floyd():
    global arr

    for k in range(n):
        for r in range(n):
            for c in range(n):
                arr[r][c] = min(arr[r][c], arr[r][k] + arr[k][c])


n = int(input())  # 도시 개수
m = int(input())  # 버스 개수

arr = [[INF] * n for _ in range(n)]

# 내 위치는 0으로 초기화
for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] = 0

for _ in range(m):
    s, e, c = map(int, input().split())  # 시작, 끝, 비용
    if arr[s - 1][e - 1] > c:
        arr[s - 1][e - 1] = c

floyd()

for r in range(n):
    for c in range(n):
        if arr[r][c] == INF:
            print(0, end=' ')
        else:
            print(arr[r][c], end=' ')
    print()