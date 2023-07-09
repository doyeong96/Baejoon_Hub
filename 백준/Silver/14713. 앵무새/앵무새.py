import sys

# sys.stdin = open("sample.txt", 'r')

from collections import deque

n = int(input())
dap = 'Impossible'
li = []
cnt = 0
empty = n
for _ in range(n):
    w = input().split()
    Q = deque(w)
    li.append(Q)
    # for i in w:
    #     Q.append(i)

t = input().split()


def sol():
    global empty

    for j in t:
        co = False
        for k in li:
            if k and k[0] == j:
                k.popleft()
                co = True
                break
        if not co:
            return False

    for k in li:
        if len(k) == 0:
            empty -= 1

    if empty != 0:
        return False
    else:
        return True


if sol():
    dap = 'Possible'
print(dap)
