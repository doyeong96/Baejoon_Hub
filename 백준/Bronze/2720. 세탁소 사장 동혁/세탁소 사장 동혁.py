t = int(input())
for i in range(t):
    money = int(input())

    q = money//25
    money = money%25
    d = money//10
    money = money%10
    n = money//5
    money = money%5
    p = money//1
    money = money%1
    print(f'{q} {d} {n} {p}')