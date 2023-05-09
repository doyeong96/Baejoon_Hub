n = int(input())
first = int(input())
stack = [first]
cnt = 0
for _ in range(n-1):
    m = int(input())
    if stack[-1] > m:
        stack.append(m)
        cnt += len(stack) - 1
    else:
        flag = True
        while flag:
            if len(stack):
                if stack[-1] <= m:
                    stack.pop()
                else:
                    stack.append(m)
                    flag = False
            else:
                stack.append(m)
                flag = False
        cnt += len(stack) - 1

print(cnt)