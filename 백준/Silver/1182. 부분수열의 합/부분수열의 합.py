def find(dep, subset):
    global cnt
    if dep == len(arr):
        li.append(subset[:])
        return

    for i in range(2):
        if not i:
            subset.append(arr[dep])
            find(dep + 1, subset)
            subset.pop()
        else:
            find(dep + 1, subset)

n, key = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
li = []
find(0, [])
# print(li)
for i in range(len(li)):
    if sum(li[i]) == key:
        cnt += 1
if key == 0:
    cnt -= 1
print(cnt)