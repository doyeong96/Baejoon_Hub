import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
psum = [[0] * (m + 1) for _ in range(n + 1)]

for r in range(1, n + 1):
    for c in range(1, m + 1):
        psum[r][c] += arr[r - 1][c - 1] + psum[r - 1][c] + psum[r][c - 1] - psum[r - 1][c - 1]
m = int(input())
for _ in range(m):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
    print(psum[r2 + 1][c2 + 1] - psum[r1][c2 + 1] - psum[r2 + 1][c1] + psum[r1][c1])
    # print(a)
