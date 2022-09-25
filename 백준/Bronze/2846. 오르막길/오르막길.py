n = int(input())
arr = list(map(int, input().split()))
li = []
maxV = 0
for i in range(n - 1):
    if arr[i] < arr[i + 1]:
        li.append([arr[i], arr[i + 1]])
        up = li[-1][1] - li[0][0]
        if maxV < up:
            maxV = up
    elif arr[i] >= arr[i + 1]:
        li = []

print(maxV)
