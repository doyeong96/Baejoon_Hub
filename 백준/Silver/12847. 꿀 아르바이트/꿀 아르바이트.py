# https://www.acmicpc.net/problem/12847
import sys

# sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

INF = 987654321
n, m = map(int, input().split())
li = list(map(int, input().split()))
ps = [0] * (n + 1)

for i in range(1, n + 1):
    ps[i] = ps[i - 1] + li[i - 1]
maxV = -INF

# print(ps)
s, e = 1, m
while e < n + 1:
    a = ps[e]
    b = ps[s-1]
    # a = ps[e] - ps[s - 1]
    # print(a-b)
    maxV = max(maxV, ps[e] - ps[s - 1])
    s += 1
    e += 1
print(maxV)
