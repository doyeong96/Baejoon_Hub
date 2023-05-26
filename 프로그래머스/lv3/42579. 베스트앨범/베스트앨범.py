def solution(genres, plays):
    answer = []
    dic = {}
    rank = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]] += plays[i]
            rank[genres[i]].append([i,plays[i]])
        else:
            dic[genres[i]] = plays[i]
            rank[genres[i]] = [[i,plays[i]]]
    # print(rank)
    # print(dic)
    ndic = sorted(dic.items(), key = lambda x:-x[1]) # 재생 횟수가 많은 순서로 정렬
    
    for i in range(len(ndic)):
        cnt = 0
        a = rank[ndic[i][0]]
        a.sort(key=lambda x:-x[1])
        for j in range(len(a)):
            answer.append(a[j][0])
            cnt+= 1
            if cnt == 2:
                break
            
    return answer