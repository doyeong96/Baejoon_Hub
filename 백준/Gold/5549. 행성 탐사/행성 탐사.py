# https://www.acmicpc.net/problem/5549
import sys

# sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

'''
풀이 아이디어
1. 자원별 구간합 배열을 생성
2. 자원별 구간합에 1씩 더해줌 => 자원이 존재하는게 먼저
    => 모든 자원을 체크한 후 다시 계산하려 했으나 변경함
3. 더해준 자원의 위치에 구간합을 계산
4. 좌표별 자원을 계산해서 출력
'''

n, m = map(int, input().split())
k = int(input())
arr = [list(input().strip()) for _ in range(n)]
O, I, J = [[0] * (m + 1) for _ in range(n + 1)], [[0] * (m + 1) for _ in range(n + 1)], [[0] * (m + 1) for _ in
                                                                                         range(n + 1)]
for r in range(1, n + 1):
    for c in range(1, m + 1):
        if arr[r - 1][c - 1] == 'O':
            O[r][c] += 1
        elif arr[r - 1][c - 1] == 'I':
            I[r][c] += 1
        else:
            J[r][c] += 1
        I[r][c] = I[r][c] + I[r - 1][c] + I[r][c - 1] - I[r - 1][c - 1]
        O[r][c] = O[r][c] + O[r - 1][c] + O[r][c - 1] - O[r - 1][c - 1]
        J[r][c] = J[r][c] + J[r - 1][c] + J[r][c - 1] - J[r - 1][c - 1]

for _ in range(k):
    r1, c1, r2, c2 = map(int, input().split())
    j = J[r2][c2] - J[r1 - 1][c2] - J[r2][c1 - 1] + J[r1 - 1][c1 - 1]
    o = O[r2][c2] - O[r1 - 1][c2] - O[r2][c1 - 1] + O[r1 - 1][c1 - 1]
    i = I[r2][c2] - I[r1 - 1][c2] - I[r2][c1 - 1] + I[r1 - 1][c1 - 1]
    print(j,o,i)
