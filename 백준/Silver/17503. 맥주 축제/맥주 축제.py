import sys
input = sys.stdin.readline

from heapq import heappop, heappush

# 기간, 선호도 합, 종류
n, m, k = map(int, input().split())
# 선호도, 도수레벨
arr = [list(map(int, input().split())) for _ in range(k)]
arr.sort(key=lambda x: (x[1], x[0]))
hq = []
# arr.sort(key=lambda x: (x[1], x[0]))
# print(arr)
do = 0
beer = 0
flag = False
for i in range(k):
    beer += arr[i][0]
    do = arr[i][1]
    heappush(hq, arr[i][0])
    if len(hq) == n:
        if beer >= m:
            flag = True
            break
        else:
            beer -= heappop(hq)

print(do) if flag else print(-1)