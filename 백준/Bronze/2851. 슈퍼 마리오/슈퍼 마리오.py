n = 10
hap = 0
li = []
for _ in range(n):
    M = int(input())
    hap += M
    li.append(hap)
    if hap >= 100:
        break
m = len(li)
# print(m)
ms1 = abs(100 - li[m-2]) # 100 - 끝에서 첫번째
ms2 = abs(100 - li[m-1]) # 100 - 끝 숫자
# 100에서 가까운 숫자가 출력 100에서 가깝다 = 100과의 차이가 적다
if ms1 == ms2:
    print(li[m-1])
elif ms1 < ms2:
    print(li[m-2])
elif ms1 > ms2:
    print(li[m-1])