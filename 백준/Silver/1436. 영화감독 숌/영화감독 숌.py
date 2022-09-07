n = int(input())
first = '666'
numbering = 0
cnt = 0
while numbering != n:
    cnt += 1
    if first in str(cnt):
        numbering += 1
print(cnt)
