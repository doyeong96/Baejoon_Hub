# https://www.acmicpc.net/problem/18870
import sys

# sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
vis = [0] * n
dic = {}
s = sorted(list(set(li)))

for i in range(len(s)):
    dic[s[i]] = i

for a in range(n):
    vis[a] = dic.get(li[a])

print(*vis)
