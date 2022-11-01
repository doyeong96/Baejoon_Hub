n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
# print(arr)
cnt = 0
l = 0
r = n - 1
while l < r:
    s = arr[l] + arr[r]
    if s == x:
        cnt += 1
        l += 1
    elif s > x:
        r -= 1
    elif s < x:
        l += 1

print(cnt)