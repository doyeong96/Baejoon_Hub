import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [input().strip() for _ in range(n)]
m = len(arr[0])
for i in range(m-1,-1,-1):
    c = set()
    for li in arr:
        a = li[i:]
        c.add(a)
    if len(c) == n:
        dap = len(a)
        break

print(dap)