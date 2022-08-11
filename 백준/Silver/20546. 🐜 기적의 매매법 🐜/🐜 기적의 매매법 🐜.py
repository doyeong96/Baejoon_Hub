money = int(input())
juga = list(map(int, input().split()))
junMoney = sungMoney = money
junStcok = sungStock = 0

for i in range(len(juga)):
    if junMoney >= juga[i]:
        junStcok += junMoney // juga[i]
        junMoney = junMoney % juga[i]

for i in range(len(juga)-3):
    if juga[i] > juga[i+1] > juga[i+2]: # 주가가 계속 하락함
        sungStock += sungMoney // juga[i+3]
        sungMoney = sungMoney % juga[i+3]
    elif juga[i] < juga[i+1] < juga[i+2]: # 주가가 계속 상승함
        sungMoney += sungStock * juga[i+2]
        sungStock = 0

junMoney = (junStcok * juga[-1]) + junMoney
sungMoney = (sungStock * juga[-1]) + sungMoney

if junMoney > sungMoney:
    print("BNP")
elif junMoney < sungMoney:
    print("TIMING")
else:
    print("SAMESAME")