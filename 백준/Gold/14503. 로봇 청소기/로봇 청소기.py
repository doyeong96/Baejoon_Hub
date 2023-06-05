# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def clean(r, c, d, cnt):
    global visit
    # 얘가 4가 되면 4방이 다 막힌거
    clean_cnt = 0
    # 현 위치는 무조껀 방문 하기 때문에 방문 처리
    visit[r][c] = 1
    while True:
        # 시작하면 무조껀 한바뀌 돔
        d = (d - 1) % 4
        nr, nc = r + dr[d], c + dc[d]
        # 다음 방향이 벽이 아니고, 청소 가능하면
        if arr[nr][nc] == 0 and visit[nr][nc] == 0:
            # 청소 하고
            visit[nr][nc] = 1
            # 한칸 전진
            r, c = nr, nc
            clean_cnt = 0
            cnt += 1
        else:
            clean_cnt += 1
        # 다음 방향이 벽 혹은 이미 청소한 상태 => 청소할 공간이 없음
        if clean_cnt == 4:
            nr, nc = r - dr[d], c - dc[d]
            if arr[nr][nc] == 0:
                r, c = nr, nc
            else:
                # break
                return cnt
            clean_cnt = 0
    # return cnt


n, m = map(int, input().split())
# 시작 좌표, 방향
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
# 현 위치는 무조껀 청소함
cnt = 1
print(clean(r, c, d, 1))