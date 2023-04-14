n = int(input())
li = sorted(list(map(int, input().split())))
s, e = 0, n - 1
Q = []
minV = float('inf')
while s < e:
    hap = li[s] + li[e]
    if abs(hap) <= minV:
        minV = abs(hap)
        Q = [li[s], li[e]]
    if hap == 0:
        break

    if hap < 0:
        s += 1
    else:
        e -= 1
print(*Q)