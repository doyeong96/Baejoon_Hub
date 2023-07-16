INF = 987654321
n, k = map(int, input().split())
li = [0] + list(map(int, input().split()))

s, e = 1, 1
dap = INF
cnt = 0
# print(li)
# if li[e] == 1:
#     cnt += 1

while s <= n + 1 and e <= n + 1:
    if cnt < k:  # 인형이 부족함
        if e < n + 1 and li[e] == 1:
            cnt += 1
        e += 1
    else:  # 인형이 충분함
        if cnt == k:
            dap = min(dap, e - s)
        if s < n + 1 and li[s] == 1:
            cnt -= 1
        s += 1
if dap == INF:
    print(-1)
else:
    print(dap)
