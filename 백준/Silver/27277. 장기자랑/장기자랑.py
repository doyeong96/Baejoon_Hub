import sys
input = sys.stdin.readline

from collections import deque

n = int(input())

li = list(map(int, input().split()))
li.sort()
Q = deque(li)
m = []

end = n-1
start = 0
while start<=end:
    m.append(Q[end])
    m.append(Q[start])
    end -= 1
    start += 1
cnt = 0
tmp = 0
for i in m:
    if tmp < i:
        cnt += i - tmp
    tmp = i
print(cnt)
