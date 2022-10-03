def bt(dep, pick):
    if len(pick) == m:
        li.add(tuple(pick))
        return
    for i in range(n):
        pick.append(arr[i])
        bt(i, pick)
        pick.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
li = set()
bt(0, [])
li = sorted(list(li))
for li in li:
    print(*li)