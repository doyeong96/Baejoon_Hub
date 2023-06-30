'''
큐에 하나도 없는 경우
=> 일단 트럭을 올리고 시간을 더해줌

큐에 하나라도 있는 경우
=> 큐가 꽉 찼을때 일단 제일 앞 트럭을 하나씩 앞으로 이동시키고 시간을 더해줌

=> 큐가 꽉 차지는 않았지만 다음 트럭을 올릴 수 없을때
    제일 앞에있는 트럭을 뺄때까지 반복해줌
    
큐에 있는 트럭이 여러개일때
=> 하나씩 앞으로 이동시킴

'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    ans = 0
    truck = deque(truck_weights)
    br = bridge_length
    Q = deque([0] * br)
    S = 0
    while Q:
        ans += 1
        S -= Q.popleft()
        
        # 큐에 트럭이 올라갈 수 있는 경우
        if truck:
            if S + truck[0] <=  weight:
                t = truck.popleft()
                S += t
                Q.append(t)
            else:
                Q.append(0)
        # 큐에 트럭이 못올라 가는 경우
        
        
    return ans