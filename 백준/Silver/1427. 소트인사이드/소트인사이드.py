arr = list(map(int, input()))
n = len(arr)

for i in range(n-1, -1, -1):
    for j in range(i):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
for k in range(n):
    print(arr[k],end='')