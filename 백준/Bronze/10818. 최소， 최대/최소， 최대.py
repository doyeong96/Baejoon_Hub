n = int(input())
num = list(map(int, input().split()))
minV = num[0]
maxV = num[0]
for i in range(1, n):
    if maxV < num[i]:
        maxV = num[i]
    if minV > num[i]:
        minV = num[i]
print(minV, maxV)