# https://www.acmicpc.net/problem/7662
import sys

# sys.stdin = open("sample.txt", 'r')
input = sys.stdin.readline

from heapq import heappop, heappush

for _ in range(int(input())):
    n = int(input())
    minQ, maxQ = [], []  # 그대로 넣는 큐, 반대로 넣는 큐
    dele = [0] * n
    for i in range(n):
        w, num = input().split()
        num = int(num)

        if w == 'I':
            heappush(minQ, (num, i))  # 작은값
            heappush(maxQ, (-num, i))  # 큰값
            dele[i] = 1
        else:
            if num == 1:  # 최대값 삭제
                # 삭제 했는데 아직 삭제 안된거 삭제
                # 그냥 삭제
                while maxQ and dele[maxQ[0][1]] == 0:
                    heappop(maxQ)
                if maxQ:
                    a = heappop(maxQ)
                    dele[a[1]] = 0
            else:  # 최소값 삭제
                while minQ and dele[minQ[0][1]] == 0:
                    heappop(minQ)
                if minQ:
                    a = heappop(minQ)
                    dele[a[1]] = 0

    # 0 인거는 지우고 1인거는 냅두고
    while minQ and dele[minQ[0][1]] == 0:
        heappop(minQ)
    while maxQ and dele[maxQ[0][1]] == 0:
        heappop(maxQ)

    if minQ and maxQ:
        print(-maxQ[0][0], minQ[0][0])
    else:
        print('EMPTY')