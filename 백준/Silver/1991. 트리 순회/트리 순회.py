def PRE(v):
    if v == 0:
        return
    if v in T:
        v = T.index(v)
        print(T[v], end='')
        PRE(L[v])
        PRE(R[v])

def IN(v):
    if v == 0:
        return
    if v in T:
        v = T.index(v)
        IN(L[v])
        print(T[v], end='')
        IN(R[v])

def POST(v):
    if v == 0:
        return
    if v in T:
        v = T.index(v)
        POST(L[v])
        POST(R[v])
        print(T[v], end='')

V = int(input())

# 왼쪽
L = [0] * (V+1)
# 오른쪽
R = [0] * (V+1)
# 트리 연결용
T = [0] * (V+1)

# 입력 받을것 T[i] 에 루트를 넣을거임
for i in range(V):
    tree = input().split()
    T[i+1] = tree[0]

    if tree[1] == '.':
        pass
    else:
        L[i+1] = tree[1]

    if tree[2] == '.':
        pass
    else:
        R[i+1] = tree[2]

PRE('A')
print()
IN('A')
print()
POST('A')