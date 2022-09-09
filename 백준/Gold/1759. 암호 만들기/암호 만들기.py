def BT(idx):
    global V, C
    # 조건을 만족했을 때 프린트해주게끔
    if len(dap) == l and V >= 1 and C >= 2:
        str(dap)
        print(''.join(dap))
        # dap.pop()
        return
        # 조건을 만족시킬 수 있게끔
    else:
        while idx != c:
            char = chars[idx]
            dap.append(char)
            if char in VS:
                V += 1
            else:
                C += 1
            BT(idx + 1)
            idx += 1
            a = dap.pop()
            if a in VS:
                V -= 1
            else:
                C -= 1

l, c = map(int, input().split())
chars = sorted(list(map(str, input().split())))
# 모음들
VS = ['a', 'e', 'i', 'o', 'u']
visted = [0] * c
# 모음 자음 갯수
V = C = 0
dap = []
# idx = 0
BT(0)
# BT()
