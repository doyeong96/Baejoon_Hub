import sys

from collections import deque

n, m, k = map(int, input().split())
li = list(map(int, input().split()))
bridge = [0] * m
time = 0
while bridge:
    time += 1
    bridge.pop(0)

    if li:
        if sum(bridge) + li[0] <= k:
            bridge.append(li.pop(0))
        else:
            bridge.append(0)
print(time)