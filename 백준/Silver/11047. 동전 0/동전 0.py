n,k = map(int,input().split())
num = []

for i in range(n):
    num.append(int(input()))

num = sorted(num,reverse=True)
cnt = 0

# while k != 0:
for i in num:
    #     if i < k:
    cnt += k//i
    k = k % i
print(cnt)