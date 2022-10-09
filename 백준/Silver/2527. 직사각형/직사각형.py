for _ in range(4):
    dap = 'a'
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    # c 일때
    if x1 == p2 and q1 == y2 or p1 == x2 and q1 == y2 or x1 == p2 and y1 == q2 or p1 == x2 and y1 == q2:
        dap = 'c'
    # d 일때
    elif p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        dap = 'd'
    # b 일떄
    # if x1 == p2 and q1 != y2 or p1 == x2 and q1 != y2 or x1 != p2 and y1 == q2 or p1 != x2 and y1 == q2:
    elif x1 == p2 or x2 == p1 or y1 == q2 or y2 == q1:
        dap = 'b'
    # 안 걸리면 a

    print(dap)