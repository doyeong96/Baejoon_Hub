import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
flag = True
while flag:
    if n % 5 == 0:
        n -= 5
        cnt += 1
    else:
        n -= 3
        cnt += 1
    if n <= 0:
        flag = False
if n == 0:
    print(cnt)
else:
    print(-1)
