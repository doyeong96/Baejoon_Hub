import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = [[0] * (n + 1) for _ in range(n + 1)]

for r in range(1, n + 1):
    for c in range(1, n + 1):
        arr2[r][c] = arr2[r - 1][c] + arr2[r][c - 1] - arr2[r - 1][c - 1] + arr[r - 1][c - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr2[x2][y2] - arr2[x2][y1 - 1] - arr2[x1 - 1][y2] + arr2[x1 - 1][y1 - 1])