winner = 0
score = 0

for i in range(5):
    scores = list(map(int, input().split()))
    if sum(scores) >= score:
        winner = i+1
        score = sum(scores)
print(winner, score)