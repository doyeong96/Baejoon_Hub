n, k = map(int, input().split())
li = list(map(int, input().split()))
cnt = [0] * (max(li) + 1)
# cnt = [0] * 200001

s, e = 0, 0
res = 0
while e < n:
    if cnt[li[e]] < k:
        cnt[li[e]] += 1
        e += 1
    else:
        cnt[li[s]] -= 1
        s += 1
    res = max(res, e - s)
print(res)