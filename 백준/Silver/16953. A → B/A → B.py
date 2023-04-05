import sys
from collections import deque


def bfs(s):
    Q = deque()
    Q.append((s, 0))
    while Q:
        num, cnt = Q.popleft()
        if int(num) > m:
            continue
        elif int(num) == m:
            return cnt + 1
        Q.append((int(num) * 2, cnt + 1))
        Q.append((str(num)+'1', cnt + 1))
    return -1

n, m = map(int, input().split())



a = bfs(n)
print(a)
