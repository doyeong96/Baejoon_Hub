stick = [64, 32, 16, 8, 4, 2, 1]

n = int(input())

cnt = 0
st = 0
now = 0
flag = True
while flag:
    a = stick[now]
    if st + a > n:
        now += 1
    else:
        st += stick[now]
        cnt += 1

    if st == n:
        flag = False

print(cnt)