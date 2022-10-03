def bt(dep, pick):
    if len(pick) == m:
        li.add(tuple(pick))
        return
    while dep != n:
        pick.append(arr[dep])
        bt(dep, pick)
        dep += 1
        pick.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
li = set()
bt(0, [])
li = sorted(list(li))
for li in li:
    print(*li)