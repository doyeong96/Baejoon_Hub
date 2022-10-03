def bt(pick):
    if len(pick) == m:
        print(*pick)
    else:
        for i in range(n):
            pick.append(arr[i])
            bt(pick)
            pick.pop()

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visit = [0] * n
bt([])