
def make_sum(dep, sub):
    # 부분집합 만들기 복습좀 하자
    if dep == len(nums):
        sum_li.add(sum(sub))
        return
    for i in range(2):
        if i:
            sub.append(nums[dep])
            make_sum(dep + 1, sub)
            sub.pop()
        else:
            make_sum(dep + 1, sub)


n = int(input())
nums = list(map(int, input().split()))
sum_li = set()
make_sum(0, [])
list(sum_li).sort()
for i in range(len(sum_li) + 2):
    if i not in sum_li:
        print(i)
        break
