def make_sum(dep, cur_sum):
    # 부분집합 만들기 복습좀 하자
    if dep == len(nums):
        sum_li.add(cur_sum)
        return
    for i in range(2):
        if i:
            make_sum(dep + 1, cur_sum+nums[dep])
        else:
            make_sum(dep + 1, cur_sum)


n = int(input())
nums = list(map(int, input().split()))
sum_li = set()
make_sum(0, 0)
list(sum_li).sort()
for i in range(len(sum_li) + 2):
    if i not in sum_li:
        print(i)
        break
