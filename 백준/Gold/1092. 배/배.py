n = int(input())
c = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
h = sorted(list(map(int, input().split())), reverse=True)

flag = True
cnt = 0
if c[0] < h[0]:
    print(-1)
    exit()
while flag:
    for i in range(n):
        if len(h) > 0:
            for j in range(len(h)):
                if c[i] >= h[j]:
                    h.pop(j)
                    break
    if len(h) == 0:
        flag = False
    cnt += 1
print(cnt)
