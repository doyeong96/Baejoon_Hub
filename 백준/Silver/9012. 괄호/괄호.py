import sys;

for _ in range(int(sys.stdin.readline())):
    stack = []
    li = list(sys.stdin.readline().rstrip())

    for i in li:
        #스택에 아무것도 없는데 닫는괄호 들어오는 상태
        if len(stack) == 0 and i == ')':
            print('NO')
            break
        else:
            if i == '(':
                stack.append(i)
            elif stack[-1] == '(' and i == ')':
                stack.pop()
    else:
        if len(stack) != 0:
            print('NO')
        else:
            print('YES')