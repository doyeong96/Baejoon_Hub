n = int(input())

for _ in range(n):
    oxlst = list(input())
    hap = 0
    cnt = 0
    for ox in oxlst:
        if ox == 'O':
            cnt += 1
            hap += cnt
        else:
            cnt = 0
    print(hap)