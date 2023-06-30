from heapq import heappush,heappop
def solution(operations):
    op = operations
    ans = []
    for x in op:
        a,b = x.split()
        b = int(b)
        # print(a,b)
        if a == 'I': # 삽입
            heappush(ans,b)
        else:
            if len(ans):
                if b == -1: # 최소값 삭제연산
                    heappop(ans)
                else: # 최대값 삭제연산
                    ans.pop()
        # print(ans)
    # print(ans)
    if ans:
        answer = [max(ans),min(ans)]
    else:
        answer = [0,0]
    # print(answer)
    return answer