from collections import deque
def solution(progresses, speeds):
    ans = []
    pro = progresses
    spd = speeds
    pQ = deque(pro)
    sQ = deque(spd)
    while pQ:
        for i in range(len(pQ)):
            cnt = 0
            pQ[i] += sQ[i]
        
        if pQ[0] >= 100:
            while len(pQ) and pQ[0] >= 100:
                pQ.popleft()
                sQ.popleft()
                cnt += 1
            ans.append(cnt)
    print(ans)
    return ans