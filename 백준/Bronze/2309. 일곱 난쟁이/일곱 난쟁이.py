nan = []
# hap = 0
for _ in range(9):
    nan.append(int(input()))
    # nan.append(int(stdin.readline()))

nan.sort()
hap = sum(nan)
for i in range(8):
    for j in range(i+1, 9):
        if hap - (nan[i] + nan[j]) == 100:
            for k in range(9):
                if k != i and k != j:
                    print(nan[k])

            exit()
