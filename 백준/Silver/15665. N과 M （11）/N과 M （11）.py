def bt(dep, pick):
    if len(pick) == m:
        print(*pick)
        return
    ov = 0
    for i in range(n):
        if ov != arr[i]:
            ov = arr[i]
            pick.append(arr[i])
            bt(i, pick)
            pick.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
li = set()
bt(0, [])