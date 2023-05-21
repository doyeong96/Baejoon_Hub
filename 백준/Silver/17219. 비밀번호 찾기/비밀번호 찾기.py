import sys

#sys.stdin = open("0000sample.txt", 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
for _ in range(n):
    a, b = input().split()
    dic[a] = b
for _ in range(m):
    a = input().strip()
    print(dic[a])
