import sys

# sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline


n = int(input())

dic = {}

for _ in range(n):
    a = input().strip()
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
b = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(b[0][0])
