def bt(now, pick):
    if len(pick) == m:
        print(*pick)
        return
    for i in range(now, n):
        pick.append(arr[i])
        bt(i, pick)
        pick.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visit = [0] * n
bt(0, [])