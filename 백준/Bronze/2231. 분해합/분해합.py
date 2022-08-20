num = int(input())
res = 0

for i in range(num+1):
    # print(i)
    hap = sum(list(map(int, str(i))))
    # print(hap)
    if num == i + hap:
        print(i)
        break
    if num == i:
        print('0')