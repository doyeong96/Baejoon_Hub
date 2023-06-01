import sys

# sys.stdin = open("0000sample.txt", 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
# print(arr)
psum = [0] * (n + 1)

for i in range(1, n + 1):
    psum[i] = arr[i - 1] + psum[i - 1]
# print(psum)
l, r = 0, 1
minv = 987654321
while True:
    if psum[r] - psum[l] >= m:
        # 여기서 최소길이 측정
        minv = min(minv, r - l)
        l += 1
    else:
        if r < n:
            r += 1
        else:
            l += 1
    if l > n:
        break
# print(minv)
print(0 if minv == 987654321 else minv)
