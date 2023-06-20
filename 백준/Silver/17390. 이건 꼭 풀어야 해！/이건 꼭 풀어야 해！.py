import sys

# sys.stdin = open("0000sample.txt", 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
li = sorted(list(map(int, input().split())))
ps = [0] * (n + 1)

for i in range(1, n + 1):
    ps[i] = ps[i - 1] + li[i - 1]

for _ in range(m):
    a,b = map(int,input().split())
    print(ps[b] - ps[a-1])
# print(li)
