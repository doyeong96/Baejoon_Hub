grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
s = 0
g = 0
for _ in range(20):
    w = list(input().split())
    a = float(w[1][0])
    if w[2] != 'P':
        s += a
        g += a * grade.get(w[2])
# print(g,s)
print(f'{g/s:.6f}')