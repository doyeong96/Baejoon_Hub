import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))
Q = deque()
cnt = [0] * n
for i in range(n):
    # 들어오는 값이 더 클때
    while Q and arr[i] < Q[-1][1]:
        Q.pop()
    # 구간을 벗어났을 떄
    # 현위치 - 구간 위치 > 범위
    while Q and  i - Q[0][0] >= m:
        Q.popleft()
    # 범위, 최소값
    Q.append((i, arr[i]))
    cnt[i] = Q[0][1] # 뭔가 최소값
print(*cnt)
