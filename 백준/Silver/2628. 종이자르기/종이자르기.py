# 10, 8
r, c = map(int, input().split()) # r c 길이를 입력
loop = int(input()) #자르는 반복 횟수
divL = []
rc = [] # r 을 자른 만큼의 길이
cc = [] # c 를 자른 만큼의 길이
for _ in range(loop):
    div, num = map(int, input().split())
    divL.append((div, num))
sortedDiv = sorted(divL, reverse=True)

for i in range(len(sortedDiv)):

    if sortedDiv[i][0] == 0:
        c2 = c - sortedDiv[i][1]
        cc.append(c2)
        c = c - c2
    else:
        r2 = r - sortedDiv[i][1]
        rc.append(r2)
        r = r - r2
else:
    cc.append(c)
    rc.append(r)

print(max(rc) * max(cc))