import sys
n, m = map(int, input().split())

left, right = 0, 1
li = [int(input()) for _ in range(n)]

li.sort()

minV = float('inf')
flag = True
while left < n and right < n:
    a = li[right] - li[left]

    # a가 m보다 작으면 오른쪽 증가, a가 m보다 크면 왼쪽 증가
    if a == m:
        minV = a
        break
    if a < m:
        right += 1
        continue
    left += 1
    minV = min(minV, a)
print(minV)

