def solution(arr):
    ans = [arr[0]]
    print(ans)
    # ans.append(arr[0])
    n = len(arr)
    
    for i in range(1,n):
        if ans[-1] != arr[i]:
            ans.append(arr[i])
    return ans