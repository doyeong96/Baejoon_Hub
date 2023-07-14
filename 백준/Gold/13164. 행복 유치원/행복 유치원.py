n, m = map(int, input().split())
li = list(map(int, input().split()))
ps = [0] * (n-1)

for i in range(n - 1):
    ps[i] = li[i + 1] - li[i]
ps.sort()
# print(ps)

cnt = 0

for i in range(n - m):
    # print(i)
    cnt += ps[i]
print(cnt)
