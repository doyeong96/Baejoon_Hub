from heapq import heappop, heappush, heapify

n, m = map(int, input().split())
li = list(map(int, input().split()))
# heap = []
heapify(li)
# for i in range(n):
#     heappush(heap, (li[i], i + 1))

for _ in range(m):
    a = heappop(li)
    b = heappop(li)
    c = a + b
    a, b = c, c
    heappush(li, a)
    heappush(li, b)

print(sum(li))