A, B = input().split()
N = len(A)
M = len(B)
arr = [['.'] * N for _ in range(M)]

for i in range(N):
    if A[i] in B:
        sero = i
        garo = B.index(A[i])
        break

for i in range(M):
    arr[i][sero] = B[i]

for i in range(N):
    arr[garo][i] = A[i]

for arr in arr:
    print(''.join(arr))
