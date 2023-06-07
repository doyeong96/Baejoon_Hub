import sys

# sys.stdin = open("0000sample.txt", 'r')
input = sys.stdin.readline
'''
1. 비어있는 칸 중에서 인접한 칸에 좋아하는 학생이 가장 많은 칸
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중 비어 있는 칸이 가장 많은 칸
3. 2를 만족하는 칸도 여러 개인 경우 행의 번호가 가장 작은 칸,
    그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
'''
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

n = int(input())
dic = {}
stus = [list(map(int, input().split())) for _ in range(n * n)]

for sut in stus:  # 좋아하는 학생 체크
    dic[sut[0]] = sut[1:]

# print(dic.items())
arr = [[0] * n for _ in range(n)]  # 학생 자리


# 현재 학생, 좋아하는 학생
def findsit(s, ls):
    pass
    # 빈자리, 좋아하는 학생 수,좌표 => 변경해야해서 작은값으로 설정해둠
    m_blank, m_like, sr, sc = -1, -1, -1, -1
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 0:
                n_blank, n_like = 0, 0
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < n:
                        if arr[nr][nc] == 0:  # 현재 위치 기준 으로 빈자리 체크
                            n_blank += 1
                        if arr[nr][nc] in ls:
                            n_like += 1

                # 1. 좋아하는 학생수가 많은거 ml <= nl, 뒤로갈수록 행열이 커지니까 같음으로 체크해야됨
                # 2. 둘이 같으면 ml == nl 빈칸 많은거
                if m_like < n_like or (m_like == n_like and m_blank < n_blank):
                    m_like, m_blank = n_like, n_blank
                    sr, sc = r, c
    return sr, sc


for s, likes in dic.items():
    r, c = findsit(s, likes)
    arr[r][c] = s
#
sa = [0, 1, 10, 100, 1000]
dap = 0
for r in range(n):
    for c in range(n):
        cnt = 0
        now = arr[r][c]
        la = dic.get(now)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] in la:
                    cnt += 1
        dap += sa[cnt]
print(dap)
