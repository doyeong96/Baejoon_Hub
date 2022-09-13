n, m = map(int, input().split())
cards = list(map(int, input().split()))
sumL = []
hap = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i] + cards[j] + cards[k] <= m:
                hap = cards[i] + cards[j] + cards[k]
                sumL.append(hap)
                hap = 0
print(max(sumL))