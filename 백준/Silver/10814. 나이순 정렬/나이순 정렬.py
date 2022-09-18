n = int(input())
p = []
for _ in range(n):
    age, name = input().split()
    p.append([age, name])
# print(p)
p.sort(key=lambda x:int(x[0]))
for p in p:
    print(*p)