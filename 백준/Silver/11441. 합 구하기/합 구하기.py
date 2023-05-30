import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
psum = [0] * (n + 1)

for i in range(1, n + 1):
    psum[i] += psum[i - 1] + arr[i - 1]
#print(psum)
for _ in range(m):
    a, b = map(int, input().split())
    print(psum[b] - psum[a-1])
