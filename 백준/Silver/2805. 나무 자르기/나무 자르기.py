n, t = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    dap = 0
    for T in tree:
        if T > mid:
            dap += T - mid
    if dap >= t:
        start = mid + 1
    else:
        end = mid - 1
print(end)