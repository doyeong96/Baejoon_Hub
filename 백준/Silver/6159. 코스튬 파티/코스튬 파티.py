
n, m = map(int, input().split())
cow = []
for _ in range(n):
    cow.append(int(input()))
cow.sort()
cnt = 0

for start in range(n):
    end = start + 1
    while end < n:
        if cow[start] + cow[end] <= m:
            cnt += 1
        end += 1
print(cnt)