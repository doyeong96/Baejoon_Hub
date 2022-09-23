def Check(item):
    for i in range(len(item)):
        for j in item[i]:
            if j >= 2:
                return 'INCORRECT'
    return 'CORRECT'

n = 9
tc = int(input())

for test in range(tc):
    try:
        check = []
        sudoku = [list(map(int, input().split())) for _ in range(n)]
        m = 3 # 작은 사각형 범위
        for r in range(n):
            rcnt = [0] * 10 # 가로검사
            for c in range(n):
                rcnt[sudoku[r][c]] += 1
            check.append(rcnt)
    
        for r in range(n):
            ccnt = [0] * 10 # 세로검사
            for c in range(n):
                ccnt[sudoku[c][r]] += 1
            check.append(ccnt)
    
        for sr in range(0, n-m+1 , 3):
            for sc in range(0, n-m+1, 3):
    
                scnt = [0] * 10  # 사각검사
                for r in range(sr, sr + m):
                    for c in range(sc, sc + m):
                        scnt[sudoku[r][c]] += 1
                check.append(scnt)
        print(f'Case {test + 1}:', end=' ')
        print(Check(check))
        input()
    except:
        break
