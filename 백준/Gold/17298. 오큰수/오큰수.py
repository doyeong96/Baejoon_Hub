import sys;

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
st = []

for i in range(n):
    while st:
        if nums[i] > nums[st[-1]]:
            nums[st[-1]] = nums[i]
            st.pop()
        else:
            st.append(i)
            break
    if len(st) == 0:
        st.append(i)
for i in st:
    nums[i] = -1

print(*nums)