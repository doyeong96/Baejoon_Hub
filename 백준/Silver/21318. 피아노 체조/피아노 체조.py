import sys

# sys.stdin = open("0000sample.txt", 'r')
input = sys.stdin.readline
from collections import deque

n = int(input())
li = list(map(int, input().split()))
m = int(input())

ps = [0] * (n + 1)

for i in range(1, n):
    if li[i - 1] > li[i]:
        a = 'mis'
    else:
        a = 'pass'

    if a == 'mis':
        ps[i] = ps[i - 1] + 1
    else:
        ps[i] = ps[i - 1]
# print(ps)
for _ in range(m):
    a,b = map(int,input().split())
    print(ps[b-1] - ps[a-1])
