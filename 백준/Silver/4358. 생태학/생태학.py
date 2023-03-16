import sys
input = sys.stdin.readline
d = {}
t = 0
while True:
    w = input().strip()
    if not w:
        break
    if w in d:
        d[w] += 1
    else:
        d[w] = 1
    t += 1
for a, b in sorted(d.items()):
    per = b / t * 100
    # print(f'{a} {round(per, 4)}')
    print("%s %.4f" %(a, per))

