import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
psum = [0] * (n + 1)
for i in range(1, n + 1):
    psum[i] += psum[i - 1] + arr[i - 1]
for _ in range(m):
    a, b = map(int, input().split())
    print(psum[b] - psum[a-1])
