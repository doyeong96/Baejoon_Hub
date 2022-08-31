dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def BFS(r, c, n): #그래프, 가로, 세로
    visited = [[0] * n for _ in range(n)]
    Q = [(r, c)]
    visited[r][c] = 1
    arr[r][c] = 0
    # cnt = 0
    cnt = 1
    # 왜 cnt가 -1씩 빠지는지 모르겠네

    while Q: #큐에 머가 있으면
        r, c = Q.pop(0) #pop0 는 왼쪽걸 반환하니까 r,c 순으로 들어왔기 때문에
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 1 and visited[nr][nc] != 1: #범위체크, 배열이 단지일때, 방문하지 않은 곳일때
                arr[nr][nc] = 0 # 0 으로 안바꿔주니까 계속 들어가서 1 갯수만큼 cnt가 들어갔던거네
                cnt += 1
                Q.append((nr, nc))
                visited[nr][nc] = 1
    return cnt

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
danzi =[] # 몇개 단지인지 len 으로 할거임

for r in range(n):
    for c in range(n):
        if arr[r][c] == 1:
            danzi.append(BFS(r, c, n))
# danzi = sorted(list(set(danzi)))
print(len(danzi))
danzi.sort()
for i in range(len(danzi)):
    print(danzi[i])
