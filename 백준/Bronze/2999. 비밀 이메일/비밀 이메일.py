word = list(input())
n = len(word)
candi = []
for x in range(1, n + 1):
    for y in range(1, n + 1):
        if x <= y and x * y == n:
            candi.append((x, y))
candi.sort(key=lambda x: x[0], reverse=True)
r = candi[0][0]
c = candi[0][1]
arr = [[0] * c for _ in range(r)]
k = 0
for i in range(c):
    for j in range(r):
        if arr[j][i] != 0:
            continue
        else:
            arr[j][i] = word[k]
            k += 1
dap = ''
for i in range(r):
    for j in range(c):
        dap += arr[i][j]
print(dap)