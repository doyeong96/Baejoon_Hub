from collections import deque


def bfs(now):
    vis = [0] * (n + 1)
    Q = deque()
    Q.append((now, 0))
    vis[now] = 1
    while Q:
        N, cnt = Q.popleft()
        for j in arr[N]:
            if vis[j] == 0:
                Q.append((j, cnt + 1))
                vis[j] = 1
    return cnt


n = int(input())
arr = [[] for _ in range(n + 1)]
while True:
    a, b = map(int, input().split())
    if a == -1:
        break
    arr[a].append(b)
    arr[b].append(a)

minV = 987654321

friend = [0] * (n + 1)
for i in range(1, n + 1):
    score = bfs(i)
    friend[i] = score
    minV = min(minV, score)
dap = []
cnt = 0
for i in range(len(friend)):
    if minV == friend[i]:
        cnt += 1
        dap.append(i)

print(minV, cnt)
print(*dap)