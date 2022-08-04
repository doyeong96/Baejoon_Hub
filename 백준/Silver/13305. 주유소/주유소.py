n = int(input())
dosi = list(map(int,input().split())) #도시 거리
girumgap = list(map(int,input().split())) #도시 기름값
price = dosi[0] * girumgap [0] #어차피 처음에는 주유하기 때문에

# dosi = dosi[1:]
# girumgap = girumgap[1:len(girumgap)-1]

mingap = girumgap[0]


for i in range(1,n-1): #0번값은 이미 계산됐기 때문에 1번 인덱스 부터 시작
    if mingap < girumgap[i]: #첫번째 기름값이 가장 싼 경우
        price += mingap*dosi[i] #기름값은 변하지 않고 모든 km를 곱한다
    else: #첫번째 기름값이 가장 싸지 않다면
        mingap = girumgap[i] #mingap 를 i번(1번) 인덱스의 기름값으로 바꾸어주고
        price += mingap*dosi[i] # 가격에 mingap*dosi[i(1)] 를 더해준다
print(price)
