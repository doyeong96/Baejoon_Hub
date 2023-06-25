# https://www.acmicpc.net/problem/19951
import sys

# sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

'''
풀이 아이디어
1. 명령을 저장할 배열 선언
2. 누적합을 저장할 배열을 선언
3. 명령을 기준으로 누적합 계산
4. 계산된 누적합 배열과 기존 연병장 높이를 가지고 연산실행
'''

n, m = map(int, input().split())
li = [0] + list(map(int, input().split()))
ps = [0] * (n + 1)
ps2 = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    ps[a - 1] += c
    ps[b] += -c
for i in range(1, n + 1):
    ps2[i] = ps[i - 1] + ps2[i - 1]

for i in range(1, n + 1):
    li[i] = li[i] + ps2[i]
print(*li[1:])
