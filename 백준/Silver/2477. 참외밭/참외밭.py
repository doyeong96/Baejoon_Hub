fruit = int(input()) #면적당 참외
allL = []
cL = [] # 세로 리스트
rL = [] # 가로 리스트
for _ in range(6): # 6각형 이라 6번
    d, meter = map(int, input().split())
    allL.append(meter)
    if d == 1 or d == 2:
        cL.append(meter)
    else:
        rL.append(meter)

# 큰 사각형 넓이
allS = max(cL) * max(rL)

#작은 사각형의 세로
mcIdx = allL.index(max(cL))

nearR1 = allL[(mcIdx - 1) % 6]
nearR2 = allL[(mcIdx + 1) % 6]

if nearR1 < nearR2:
    cutR = nearR2 - nearR1
else:
    cutR = nearR1 - nearR2
# cutR 작은사각형의 세로

#작은 사각형의 가로
mrIdx = allL.index(max(rL))

nearC1 = allL[(mrIdx - 1) % 6]
nearC2 = allL[(mrIdx + 1) % 6]

if nearC1 < nearC2:
    cutC = nearC2 - nearC1
else:
    cutC = nearC1 - nearC2
    
# cutC 작은 사각형의 가로

cutS = cutR * cutC

bap = allS - cutS

print(bap*fruit)