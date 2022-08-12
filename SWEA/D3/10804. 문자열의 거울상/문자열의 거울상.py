tc = int(input())
for test in range(tc):
    arr = list(input())
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
    for i in range(n):
        if arr[i] == 'q':
            arr[i] = 'p'
        elif arr[i] == 'p':
            arr[i] = 'q'
        elif arr[i] == 'b':
            arr[i] = 'd'
        elif arr[i] == 'd':
            arr[i] = 'b'
    arr = ''.join(arr)
    print(f'#{test+1} {arr}')