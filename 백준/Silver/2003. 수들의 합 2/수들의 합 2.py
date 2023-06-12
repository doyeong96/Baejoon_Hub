import sys

# sys.stdin = open("0000sample.txt", 'r')
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
li = list(map(int, input().split()))
ps = [0] * (n + 1)

for i in range(1, n + 1):
    ps[i] = li[i - 1] + ps[i - 1]

s, e = 0, 1
cnt = 0
while e <= n:
    a = ps[e] - ps[s]
    if a == m:
        cnt += 1
        s += 1
    elif a < m:
        e += 1
    else:
        s += 1
print(cnt)
