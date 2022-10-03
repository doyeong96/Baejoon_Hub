def bt(dep, pick):
    if len(pick) == m:
        print(*pick)
        return
    over = 0
    for i in range(dep, n):
        if over != arr[i]:
            over = arr[i]
            pick.append(arr[i])
            bt(i, pick)
            pick.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
bt(0, [])