nums = input().split('-') #식을 입력받는다
hap1 = 0 # -를 만나기 전 숫자들의 합
hap2 = 0 # -를 만난 후 숫자들의 합

# dap = sum(num[0])
# print(nums)

# print(nums[1:])
for i in map(int,nums[0].split('+')): #-를 만나기 전 숫자들은 nums[0]
    hap1 += i

for i in nums[1:]: # - 이후의 숫자들은 어차피 쭉 - 이므로
    # i = list(map(int,i.split('+'))) # 연산자를 신경쓰지 않고 리스트에 담아준 뒤
    # hap2 = (sum(i)) # 합계를 구하고
    for j in map(int,i.split('+')):
        hap2 -= j
dap = hap1 + hap2 #처음 합과 이후 합을 빼준다
print(dap)