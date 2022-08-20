numA, numB = input().split()
n = 3
a = []
b = []
for i in range(n):
    a.append(numA[n-i-1])
    b.append(numB[n-i-1])
# a, b = int(''.join(a)), int(''.join(b))
a, b = ''.join(a), ''.join(b)

if a < b:
    print(b)
else:
    print(a)
