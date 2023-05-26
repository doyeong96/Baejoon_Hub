from collections import deque
def solution(prices):
    answer = []
    Q = deque(prices)
    
    while Q:
        a = Q.popleft()
        cnt = 0
        for q in Q:
            cnt += 1
            if a > q:
                break
        answer.append(cnt)
    return answer