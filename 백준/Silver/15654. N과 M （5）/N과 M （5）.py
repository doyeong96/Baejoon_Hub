def bt(pick):
    global visit

    if len(pick) == m:
        print(*pick)
        return
    else:
        for i in range(n):
            if visit[i] == 0:
                pick.append(arr[i])
                visit[i] = 1
                bt(pick)
                pick.pop()
                visit[i] = 0


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visit = [0] * n
bt([])
