n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)
arr.sort(key=lambda x: (x[1], x[0]))
for arr in arr:
    print(*arr)