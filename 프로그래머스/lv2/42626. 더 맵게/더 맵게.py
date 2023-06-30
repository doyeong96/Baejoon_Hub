from heapq import heappush, heappop,heapify
def solution(scoville, K):
    ans = 0
    sco = scoville
    stil = []
    heapify(sco)
    flag = True
    while flag:
        # ans += 1
        # print(sco)
        
        a = heappop(sco)
        b = heappop(sco)
        c = a + (b*2)
        # print(c)
        if a < K or b < K:
            ans +=1
        heappush(sco,c)
        # print(sco)
        if len(sco) == 1:
            flag = False
            if sco[0]<K:
                ans = -1
    
    return ans