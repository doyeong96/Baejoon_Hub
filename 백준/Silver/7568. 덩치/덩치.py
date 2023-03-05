n = int(input())
# people = [(w,h) map(int, input().split()) for _ in range(n)]
people = []
for _ in range(n):
    w, h = map(int, input().split())
    people.append((w, h))
cnt = 1
rank = []
for i in range(n):
    for j in range(n):
        # 비교하는 친구가 나보다 몸무게가 많이나가고
        if people[i][0] < people[j][0]:
            # 비교하는 친구의 키가 나보다 클때
            if people[i][1] < people[j][1]:
                cnt += 1
    rank.append(cnt)
    cnt = 1
print(*rank)