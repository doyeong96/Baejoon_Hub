from collections import deque
def solution(priorities, location):
    pro,loc=priorities, location
    answer = 0
    Q = deque()
    
    
    for i in enumerate(pro):
        Q.append(i)
    
    pro.sort(reverse=True)
    
    # print(pro)
    # print(Q)
    flag = True
    cnt = 1
    while flag:
        a = Q.popleft()
        # print(a)
        if a[1] == pro[0]:
            if a[0] == loc:
                answer = cnt
                break
            else:
                pro.pop(0)
                cnt += 1
        else:
            Q.append(a)            
    return answer