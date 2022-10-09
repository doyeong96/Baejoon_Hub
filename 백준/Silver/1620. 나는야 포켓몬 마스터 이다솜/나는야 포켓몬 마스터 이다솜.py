import sys
input = sys.stdin.readline

n, m = map(int, input().split())
puki = [input().strip() for _ in range(n)]
puki_dick = {puki[i]: i + 1 for i in range(n)}

for i in range(m):
    dap = input().strip()
    if dap.isdigit():
        find = int(dap)
        print(puki[find-1])
    else:
        print(puki_dick.get(dap))