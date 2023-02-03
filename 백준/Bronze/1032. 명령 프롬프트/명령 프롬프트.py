n = int(input())
a = list(input())

for i in range(n-1):
    b = list(input())
    for i in range(len(a)):
        if a[i] != b[i]:
            a[i] = '?'
for a in a:
    print(a,end='')