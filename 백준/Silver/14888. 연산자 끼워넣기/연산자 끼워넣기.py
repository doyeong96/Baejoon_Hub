def calc(dep, val):
    global minV, maxV
    if dep == n - 1:
        # 결과 확인
        minV = min(minV, val)
        maxV = max(maxV, val)
    else:
        num = nums[dep + 1]
        calcli = [val + num, val - num, val * num, int(val / num)]
        # 연산자는 4개
        for i in range(4):
            if op[i] != 0:
                op[i] -= 1
                calc(dep + 1, calcli[i])
                op[i] += 1


n = int(input())
m = n - 1
# OP = []
# visit = [0] * (n + m)
# find = []
# + - * //
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
# make_operater()
minV = 987654321
maxV = -987654321
calc(0, nums[0])
print(maxV)
print(minV)
