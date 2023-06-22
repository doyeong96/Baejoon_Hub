# https://www.acmicpc.net/problem/16507
import sys

# sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

'''
풀이 아이디어
1. 구간합 배열을 생성
2. 좌표의 구간합을 체크
3. 좌표의 넓이를 계산
4. 구간합과 넓이를 나눔
'''

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ps = [[0] * (m + 1) for _ in range(n+1)]

for r in range(1, n + 1):
    for c in range(1, m + 1):
        ps[r][c] += arr[r - 1][c - 1] + ps[r - 1][c] + ps[r][c - 1] - ps[r - 1][c - 1]
#
# for p in ps:
#     print(p)

for _ in range(k):
    r1, c1, r2, c2 = map(int, input().split())
    S = ps[r2][c2] - ps[r1 - 1][c2] - ps[r2][c1 - 1] + ps[r1 - 1][c1 - 1]
    C = (r2 - r1 + 1) * (c2 - c1 + 1)
    print(S // C)
