n = int(input())
# time = [listinput().split() for _ in range(n)]
time = [list(map(int, input().split())) for _ in range(n)]
time = sorted(time, key=lambda x: (x[1], x[0]))
cnt = 1
end = time[0][1]
for i in range(1, n):
    if end <= time[i][0]:
        cnt += 1
        end = time[i][1]
print(cnt)