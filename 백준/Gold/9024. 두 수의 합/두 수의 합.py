for _ in range(int(input())):
    n, k = map(int, input().split())
    li = sorted(list(map(int, input().split())))
    # print(li)
    cnt = 0
    arr = []
    s, e = 0, n - 1

    while s < e:
        a = li[s] + li[e]
        if li[s] + li[e] == k:
            s += 1
            e -= 1
            arr.append(0)
        elif li[s] + li[e] < k:
            arr.append(abs(k - (li[s] + li[e])))
            s += 1
        elif li[s] + li[e] > k:
            arr.append(abs(k - (li[s] + li[e])))
            e -= 1
    arr.sort()
    minV = min(arr)
    for i in arr:
        if i == minV:
            cnt +=1
    print(cnt)
