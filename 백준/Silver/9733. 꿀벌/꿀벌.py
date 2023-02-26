import sys


input = sys.stdin.readlines

lines = list(input())
cnt = 0
bee = {'Re': 0, 'Pt': 0, 'Cc': 0, 'Ea': 0, 'Tb': 0, 'Cm': 0, 'Ex': 0}
for line in lines:
    line = list(line.split())
    for i in line:
        cnt += 1
        if i in bee:
            bee[i] += 1
        else:
            continue

# print(bee)
for key, val in bee.items():
    print(f'{key} {val} {val / cnt:.2f}')
print(f'Total {cnt} 1.00')
