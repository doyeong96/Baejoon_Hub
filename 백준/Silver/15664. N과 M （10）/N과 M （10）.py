def bt(dep, pick):
    if len(pick) == m:
        li.add(tuple(pick))
        return
    while dep != n:
        # if visit[dep] == 0:
        # visit[dep] = 1
        pick.append(arr[dep])
        bt(dep + 1, pick)
        dep += 1
        pick.pop()
        # visit[dep] = 0


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visit = [0] * n
li = set()
bt(0, [])
li = sorted(list(li))
for li in li:
    print(*li)
