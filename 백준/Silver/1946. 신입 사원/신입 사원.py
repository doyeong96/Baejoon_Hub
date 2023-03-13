import sys

input = sys.stdin.readline
# 적어도 하나가 다른 지원자보다 떨어지지 않는 자
for _ in range(int(input())):
    n = int(input())
    # 서류량 면접 순위임
    li = [list(map(int, input().split())) for _ in range(n)]
    li.sort(key=lambda x: (x[0], x[1]))
    # print(li)
    cnt = 1
    now = li[0]
    for i in range(1, n):
        if now[0] < li[i][0] and now[1] < li[i][1]:
            continue
        else:
            cnt += 1
            now = li[i]
    print(cnt)
