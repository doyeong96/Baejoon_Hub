# https://www.acmicpc.net/problem/1935
import sys

# sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

n = int(input())
li = list(input().strip())
st = [int(input()) for _ in range(n)]

num = []
# print(ord('A')-64)
calc = ['*', '/', '+', '-']
for j in range(len(li)):
    if li[j] not in calc:
        num.append(st[ord(li[j]) - 65])
    else:
        a = num.pop()
        b = num.pop()

        if li[j] == calc[0]:
            b *= a
        elif li[j] == calc[1]:
            b /= a
        elif li[j] == calc[2]:
            b += a
        else:
            b -= a
        num.append(b)
print(f'{num[-1]:.2f}')
