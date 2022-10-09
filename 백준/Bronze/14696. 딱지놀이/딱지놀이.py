n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = a[1:]
    a1 = a.count(1)
    a2 = a.count(2)
    a3 = a.count(3)
    a4 = a.count(4)
    b = b[1:]
    b1 = b.count(1)
    b2 = b.count(2)
    b3 = b.count(3)
    b4 = b.count(4)
    # 무승부 일때
    # if a4 == b4 and a3 == b3 and a2 == b2 and a1 == b1:
    #     pass
    if a4 > b4:
        print('A')
        continue
    elif b4 > a4:
        print('B')
        continue
    else:
        if a3 > b3:
            print('A')
            continue
        elif b3 > a3:
            print('B')
            continue
        else:
            if a2 > b2:
                print('A')
                continue
            elif b2 > a2:
                print('B')
                continue
            else:
                if a1 > b1:
                    print('A')
                    continue
                elif b1 > a1:
                    print('B')
                    continue
                else:
                    print('D')
