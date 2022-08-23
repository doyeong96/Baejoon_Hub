def postfix(num):
    stack = []
    result = []
    # result = ''
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0} # 스택 안의 우선순위
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3} # 스택 밖에서 들어올때 우선순위
    # stack.append(num[0])
    for i in range(len(num)):
        # 연산자일때
        if num[i] in '+-*/()':
            #스택 비어있으면 그냥 넣음
            if len(stack) == 0:
                stack.append(num[i])
            #스택 차있으면 우선순위를 확인하고 넣음
            else:
                # 닫는 괄호 처리
                if num[i] == ')':
                    while stack[-1] != '(':
                        result.append(stack.pop())
                        # result += stack.pop()
                    stack.pop()
                # elif num[i] == '+-*/(':
                else:
                    # 스택이 차있고 스택의 가장 마지막 원소의 우선순위가
                    # 들어가고자 하는 우선순위보다 크거나 같을때
                    while stack and isp[stack[-1]] >= icp[num[i]]:
                        # result += stack.pop()
                        result.append(stack.pop())
                    stack.append(num[i])
        # 숫자면
        else:
            result.append(num[i])
            # result += stack.pop()
            # result += num[i]
    while stack: #비어있지 않으면 스택에 남아있는 요소 전부 꺼내서 붙이기
        result.append(stack.pop())
        # result += stack.pop()
    return ''.join(result)

numbers = list(map(str, input()))
print(postfix(numbers))