n = int(input())
arr = list(map(int, input().split()))
cnt = []
for i in range(n):
    cnt.insert(arr[i], i + 1)

print(*cnt[::-1])
