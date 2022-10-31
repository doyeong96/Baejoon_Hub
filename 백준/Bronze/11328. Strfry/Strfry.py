for _ in range(int(input())):
    a, b = input().split()
    A = list(a)
    B = list(b)
    dap = 'Possible'
    cnt = 0
    if len(A) != len(B):
        dap = 'Impossible'
    else:
        while A:
            i = A.pop()
            for j in range(len(B)):
                if i == B[j]:
                    cnt += 1
                    B.pop(j)
                    break
    if cnt != len(a):
        dap = 'Impossible'

    print(dap)
