from heapq import heappop, heappush

n = int(input())
li = []
cnt = 1
for _ in range(n):
    start, end = map(int, input().split())
    li.append([start, end])

# 시작 시간이 가장 빠른 강의가 먼저 오게
li.sort(key=lambda x: (x[0], x[1]))
Q = []
#
heappush(Q, li[0][1])


for i in range(1, n):
    # 현재 강의가 끝나는 시간
    time = Q[0]
    # 다른 강의 시간보다 늦게끝나는 경우
    if time > li[i][0]:
        heappush(Q, li[i][1])
    else:
        heappop(Q)
        heappush(Q, li[i][1])
print(len(Q))