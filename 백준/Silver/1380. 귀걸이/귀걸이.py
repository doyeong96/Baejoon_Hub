# https://www.acmicpc.net/problem/1380
import sys

# sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

cnt = 1
while True:
    n = int(input())

    if n == 0:
        break
    name = [0] * (n + 1)
    for i in range(n):
        name[i + 1] = input().strip()

    call = {}
    for _ in range(2 * n - 1):
        a, b = input().split()
        a = int(a)
        if a in call:
            call[a] += 1
        else:
            call[a] = 1

    for x, y in call.items():
        if y % 2 == 1:  # 못찾음
            print(cnt, name[x])
    cnt += 1