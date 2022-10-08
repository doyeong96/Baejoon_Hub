n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()

maxV = -987654321
down = 1
up = 1
find = []
for i in range(n-1):
    if arr[i] <= arr[i+1]:
        up += 1
        if maxV < up:
            maxV = up
    else:
        up = 1
    if arr[i] >= arr[i+1]:
        down += 1
        if maxV < down:
            maxV = down
    else:
        down = 1
print(maxV)
