import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
# maxV = -987654321
res = []
res.append(sum(arr[:k]))

for i in range(n - k):
    res.append(res[-1] - arr[i] + arr[i + k])
    # print(arr[i:i+k])
# print(res)
print(max(res))