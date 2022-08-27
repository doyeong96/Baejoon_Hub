n, k = map(int, input().split())

student = []
studentdic = {}
cnt = 0
for _ in range(n):
    s, y = map(int, input().split())
    student.append((s, y))
student.sort()
for i in student:
    if i in studentdic:
        studentdic[i] += 1
    else:
        studentdic[i] = 1

for val in studentdic.values():
    while val != 0:
        if k < val:
            cnt += 1
            val = val - k
        else:
            cnt += 1
            val = val - val
print(cnt)