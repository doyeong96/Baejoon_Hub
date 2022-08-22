n = int(input())
numL = []
for _ in range(n):
    numL.append(int(input()))
numL.sort()
for i in range(n):
    print(numL[i])