N, T = map(int, input().split())
# 타겟 국가
TC = []
# 나머지 국가
EC = []
for i in range(N):
    c, g, s, b = map(int, input().split())
    if c == T:
        TC.append([c, g, s, b])
    else:
        EC.append([c, g, s, b])

# 금메달 기준 정렬
EC = sorted(EC, key=lambda x: x[1], reverse=True)
rank = 1
for i in range(len(EC)):
    # 금 금이 타겟 국가 보다 크면 타겟 국가의 랭크는 떨어짐
    if EC[i][1] > TC[0][1]:
        rank += 1
    # 금 갯수가 동일 하면
    elif EC[i][1] == TC[0][1]:
        # 은 비교
        if EC[i][2] > TC[0][2]:
            rank += 1
        elif EC[i][2] == TC[0][2]:
            # 동 비교
            if EC[i][3] > TC[0][3]:
                rank += 1
print(rank)