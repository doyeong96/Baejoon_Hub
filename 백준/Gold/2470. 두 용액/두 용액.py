import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort()

flag = True
minV = float('inf')
left, right = 0, n - 1
while flag:
    hap = li[left] + li[right]

    if minV > abs(hap):
        minV = abs(hap)
        a, b = li[left], li[right]

    if hap > 0:
        right -= 1
    else:
        left += 1
    if left >= right:
        flag = False
print(a, b)
