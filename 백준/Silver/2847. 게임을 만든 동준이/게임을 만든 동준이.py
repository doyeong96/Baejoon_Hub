cnt = 0
n = int(input())
score = [int(input()) for _ in range(n)]
for i in range(n - 1, 0, -1):
    while score[i] <= score[i - 1]:
        score[i - 1] = score[i - 1] - 1
        cnt += 1
print(cnt)