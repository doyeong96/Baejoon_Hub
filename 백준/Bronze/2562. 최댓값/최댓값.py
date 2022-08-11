num = []
for i in range(9):
    num.append(int(input()))

maxIdx = 0
for i in range(9):
    if num[maxIdx] < num[i]:
        maxIdx = i
print(num[maxIdx])
print(maxIdx+1)