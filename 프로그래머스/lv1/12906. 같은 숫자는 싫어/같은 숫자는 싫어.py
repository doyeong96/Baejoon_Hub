def solution(arr):
    ans = []
    ans.append(arr[0])
    n = len(arr)
    
    for i in range(1,n):
        if ans[-1] != arr[i]:
            ans.append(arr[i])
    return ans