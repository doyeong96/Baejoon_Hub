n = int(input())
nums = list(map(int, input().split()))
m = int(input())
T_nums = list(map(int, input().split()))
nums = set(nums)
'''
T_nums 의 숫자가
nums에 있는지를 출력해야함
'''
for i in range(m):
    if T_nums[i] in nums:
        print(1)
    else:
        print(0)