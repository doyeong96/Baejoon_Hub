n = int(input())
switch = list(map(int, input().split()))
num = int(input())
for _ in range(num):
    S, SN = map(int, input().split())
    # 남자일 경우 자기가 받은 숫자의 배수를 변경
    if S == 1:
        m = 1
        sn = SN * m # sn = 변경할 스위치의 위치
        while sn <= n: # 변경할 위치가 스위치 총 길이보다 작을때만 돌아감
            sn = SN * m
            if sn <= n:
                if switch[sn - 1] == 0:
                    switch[sn - 1] = 1
                else:
                    switch[sn - 1] = 0
            m += 1
        pass

    # 여자일 경우 받은 숫자의 좌우를 체크
    # 대칭이면 대칭인 부분 + 받은 숫자 위치 전부 변경
    # 비대칭이면 받은 숫자만 변경
    else:
        # 여자의 경우 받은 숫자 좌우를 체크해주기 때문에 굳이 곱할필요 없음(새로운 변수 안만듬)
        if switch[SN - 1] == 0:
            switch[SN - 1] = 1
        else:
            switch[SN - 1] = 0
        i = 0
        while True:
            if SN - 2 - i < 0 or SN + i >= n:
                break
            else:
                if switch[SN - 2 - i] != switch[SN + i]:
                    break
                else:
                    if switch[SN - 2 - i] == 0 and switch[SN + i] == 0:
                        switch[SN - 2 - i] = 1
                        switch[SN + i] = 1
                    else:
                        switch[SN - 2 - i] = 0
                        switch[SN + i] = 0
            i += 1
for i in range(0, n, 20):
    print(*switch[i:20 + i])