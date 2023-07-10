n = int(input())
num = n
# new = 0
flag = True
cnt = 0
while flag:
    cnt += 1
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    new = (b * 10) + c
    num = new
    if num == n:
        flag = False

print(cnt)