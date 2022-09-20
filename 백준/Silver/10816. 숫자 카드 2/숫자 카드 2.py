n = int(input())
#상근이가 가지고있는 숫자카드
nums = list(map(int, input().split()))
m = int(input())
#몇개 가지고 있는지 구분해야 할 숫자카드
T_nums = list(map(int, input().split()))
dict = {}

for nums in nums:
    if nums in dict:
        dict[nums] += 1
    else:
        dict[nums] = 1
for i in T_nums:
    if i in dict:
        print(dict[i], end=' ')
    else:
        print(0, end=' ')