'''
0번 1번 비교해서 같으면
'''
n = int(input())
cnt = 0
for i in range(n):
    word = input()
    error = 0 #첫글자가 2번째 글자 이후에 있으면 에러 증가
    m = len(word)
    for j in range(m-1):
        if word[j] == word[j+1]: # 이어지는 단어면 그냥 넘어가고
            pass
        elif word[j] in word[j+1:]: 
            # 이어지지 않는 단어일 경우 j 번째 글자가 j 번 이후에 있으면 안되니까 에러 1증가
            error += 1
    if error == 0: # 에러가 없을때만 카운트 증가
        cnt += 1
print(cnt)