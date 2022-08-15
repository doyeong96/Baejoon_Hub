n = int(input())
score = list(map(int, input().split()))
m = score[0]
cScore = []
hap = 0
for i in range(n):
    if m < score[i]:
        m = score[i]
for j in range(n):
    cScore.append((score[j]/m)*100)
    hap += cScore[j]
avg = hap/n
print(avg)