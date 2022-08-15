n = 10
target = 42

num = [int(input()) for _ in range(n)]
new = []
cnt = 0
for i in range(n):
    if num[i] % target not in new:
        new.append(num[i] % target)
print(len(new))