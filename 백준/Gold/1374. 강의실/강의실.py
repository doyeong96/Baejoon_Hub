from heapq import heappop, heappush

li = []
room = []
n = int(input())
for _ in range(n):
    a, start, end = map(int, input().split())
    heappush(li, (start, end))
start, end = heappop(li)
heappush(room, end)
while li:
    start, end = heappop(li)
    if room[0] <= start:
        heappop(room)
    heappush(room, end)
print(len(room))
