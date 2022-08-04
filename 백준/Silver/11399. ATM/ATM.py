n = int(input())
num = list(map(int,input().split()))
ghap = 0
hap = []
num.sort()

for i in range(n):
    ghap += num[i]
    hap.append(ghap)
print(sum(hap))