n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
B = list(map(int, input().split()))
S = 0
for i in range(n - 1, -1, -1):
    S += A[i] * max(B)
    A.pop()
    B.pop(B.index(max(B)))

print(S)
