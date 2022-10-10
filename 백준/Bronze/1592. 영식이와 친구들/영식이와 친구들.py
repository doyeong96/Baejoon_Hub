n, m, l = map(int, input().split())
arr = [0] * n
cnt = 0
i = 0
arr[i] = 1
while arr[i] != m:
    # 홀수 => 시계방향(오른쪽)
    if arr[i] % 2 == 1:
        i = (i + l) % n
        arr[i] += 1
        cnt += 1
    # 짝수 => 반시계 방향(왼쪽)
    else:
        i = (i - l) % n
        arr[i] += 1
        cnt += 1
print(cnt)
