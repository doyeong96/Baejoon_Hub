n = int(input())
li = list(map(int,input().split()))
cnt = 0
flag = True
while flag:
    MAX = -987654321
    for i in range(n):
        MAX = max(MAX, abs(li[cnt] - li[i]))
    print(MAX)
    cnt += 1
    if cnt == n:
        flag = False