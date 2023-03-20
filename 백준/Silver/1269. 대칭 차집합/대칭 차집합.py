import sys

input = sys.stdin.readline

n, m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
dic = {}
for a in al:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

for b in bl:
    if b in dic:
        dic[b] += 1
    else:
        dic[b] = 1
cnt = 0
for val in dic.values():
    if val == 1:
        cnt += 1
print(cnt)
