import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
pos, neg = [], []
last = 0
for i in li:
    last = max(abs(i), last)
    if i < 0:
        neg.append(abs(i))
    else:
        pos.append(i)
res = 0
pos.sort(reverse=True)
neg.sort(reverse=True)
for i in range(0, len(pos), m):
    res += pos[i] * 2
for i in range(0, len(neg), m):
    res += neg[i] * 2
print(res-last)