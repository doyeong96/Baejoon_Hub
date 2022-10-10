L = int(input())
n = int(input())
cake = [0] * (L + 1)
want_maxV = 0
want_max = 0
real_max = 0
real_maxV = 0
for i in range(1, n + 1):
    p, k = map(int, input().split())
    for j in range(p, k + 1):
        # 많이 받기를 기대한 사람
        if want_maxV < k - p:
            want_maxV = k - p
            want_max = i

        if cake[j] == 0:
            cake[j] = i

for i in range(1, n + 1):
    cnt = 0
    for j in range(len(cake)):
        if cake[j] == i:
            cnt += 1
    if real_maxV < cnt:
        real_maxV = cnt
        real_max = i

print(want_max)
print(real_max)
