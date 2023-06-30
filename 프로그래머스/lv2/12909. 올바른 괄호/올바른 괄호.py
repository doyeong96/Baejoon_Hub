def solution(s):
    answer = True
    st = []

    for i in s:
        if not st and i == ')': # 비어있는 상태에서 빈괄호
            # print('1')
            return False
        else:
            if not st:
                # print('2')
                st.append(i)
                
            
            elif st[-1] == '(': # 여는괄호의 경우
                if i == ')':
                    # print('3')
                    st.pop()
                elif i == '(':
                    # print('4')
                    st.append(i)
            else: # 닫는 괄호의 경우
                if i == ')':
                    # print('5')
                    return False
                else:
                    # print('6')
                    st.append(i)
        # print()
    # print(st
    if st:
        return False
    return True