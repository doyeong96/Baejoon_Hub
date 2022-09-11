while 1:
    word = input()
    stack = []
    if word == '.':
        break
    for i in range(len(word)):
        # 비어 있는데 닫는 괄호
        if len(stack) == 0 and word[i] == ')' or len(stack) == 0 and word[i] == ']':
            stack.append('.')
            break

        elif word[i] == '(' or word[i] == '[':
            stack.append(word[i])
        elif len(stack) != 0:
            if stack[-1] == '(' and word[i] == ')' or stack[-1] == '[' and word[i] == ']':
                stack.pop()
            elif stack[-1] == '(' and word[i] == ']' or stack[-1] == '[' and word[i] == ')':
                stack.append(word[i])

    if len(stack) == 0:
        print('yes')
    else:
        print('no')