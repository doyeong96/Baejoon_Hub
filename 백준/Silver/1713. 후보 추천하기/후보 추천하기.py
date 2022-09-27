n = int(input())
m = int(input())
reco = list(map(int, input().split()))
# 사진 틀
pic = []
# 카운트
cnt = [0] * 101
# 현재 삭제해야 하는 학생 위치

for i in range(m):
    # 사진이 꽉 차있지 않은 상태
    if len(pic) != n:
        # 추천이 연달아서 이어질수도 있기 때문에 사진틀에 없는 경우에만 추가
        if reco[i] not in pic:
            pic += [reco[i]]
        cnt[reco[i]] += 1
    else:
        # 사진이 꽉 찬 경우

        # 이미 사진틀에 있는 학생이 추천을 또 받음
        if reco[i] in pic:
            cnt[reco[i]] += 1
            continue
        else:
        # 사진틀에 없는 학생이 추천을 받음
            maxV = 987654321
            for j in pic:
                if maxV > cnt[j]:
                    maxV = cnt[j]
                    target = j
            else:
                pic.pop(pic.index(target))
                cnt[target] = 0
                pic += [reco[i]]
                cnt[reco[i]] += 1
pic.sort()
print(*pic)