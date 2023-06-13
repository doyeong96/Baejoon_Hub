import sys

# sys.stdin = open("0000sample.txt", 'r')
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())

li = [0] * (n + 1)
for _ in range(k):
    a = int(input())
    li[a] = 1
ps = [0] * (n + 1)
for i in range(1, n + 1):
    ps[i] = ps[i - 1] + li[i]
# print(li)
# print(ps)
s, e = 1, m  # 시작구간, 끝구간
cnt = n
while e <= n:
    S = ps[e] - ps[s - 1]
    s += 1
    e += 1
    if cnt > S:
        cnt = S

print(cnt)
