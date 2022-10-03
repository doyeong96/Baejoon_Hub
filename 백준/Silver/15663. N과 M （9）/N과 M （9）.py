def bt(pick):
    if len(pick) == m:
        li.add(tuple(pick))
        return
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            pick.append(arr[i])
            bt(pick)
            pick.pop()
            visit[i] = 0

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visit = [0] * n
li = set()
bt([])
li = sorted(list(li))
for li in li:
    print(*li)