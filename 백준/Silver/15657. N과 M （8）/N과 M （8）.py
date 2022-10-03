def bt(dep, pick):
    if len(pick) == m:
        print(*pick)
        return
    else:
        while dep != n:
            pick.append(arr[dep])
            bt(dep, pick)
            pick.pop()
            dep += 1


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visit = [0] * n
bt(0, [])