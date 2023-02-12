import sys


input = sys.stdin.readline
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
import heapq

n = int(input())
li = []
for _ in range(n):
    a = -int(input())
    heapq.heappush(li, a)
    if a == 0:
        if li:
            print(abs(heapq.heappop(li)))
        else:
            print(0)
