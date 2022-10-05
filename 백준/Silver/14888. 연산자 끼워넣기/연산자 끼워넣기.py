def make_operater():
    # 연산자 만들기
    for i in range(4):
        while op_num[i] != 0:
            if i == 0:
                OP.append('+')
                op_num[i] -= 1
            elif i == 1:
                OP.append('-')
                op_num[i] -= 1
            elif i == 2:
                OP.append('*')
                op_num[i] -= 1
            elif i == 3:
                OP.append('/')
                op_num[i] -= 1


def make_op(k):
    global visit, find
    if k == len(OP):
        op_set.add(tuple(OP))
    else:
        for i in range(k, len(OP)):
            OP[k], OP[i] = OP[i], OP[k]
            make_op(k + 1)
            OP[k], OP[i] = OP[i], OP[k]


def calc():
    global op_set, maxV, minV
    op_li = list(op_set)
    while True:
        for i in range(len(op_li)):
            calc_num = nums[:]
            for j in range(len(op_li[i])):
                a = calc_num.pop(0)
                b = calc_num.pop(0)
                o = op_li[i][j]
                if o == '+':
                    ab = a + b
                elif o == '-':
                    ab = a - b
                elif o == '*':
                    ab = a * b
                elif o == '/':
                    ab = int(a / b)
                calc_num.insert(0, ab)
            find.append(*calc_num)
            calc_num.clear()
        if i == len(op_li) - 1:
            break
    maxV = max(max(find), maxV)
    minV = min(min(find), minV)

n = int(input())
m = n - 1
OP = []
visit = [0] * (n + m)
find = []
op_set = set()
# + - * //
nums = list(map(int, input().split()))
op_num = list(map(int, input().split()))
make_operater()
minV = 987654321
maxV = -987654321
make_op(0)
calc()
print(maxV)
print(minV)
