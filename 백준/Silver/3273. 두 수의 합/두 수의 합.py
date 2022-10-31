'''
9
5 12 7 10 9 1 2 3 11
13
'''
n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
# print(arr)
cnt = 0
# while l != r:
#     if arr[l] + arr[r] == x:
#         cnt += 1
#         r += 1
#     else:
#         r += 1
#     if r == end:
#         l += 1
#         r = l + 1
# slow = 0
# while True:
#     for fast in range(slow+1, n):
#         if arr[slow] + arr[fast] == x:
#             cnt += 1
#     else:
#         slow += 1
#     if slow == n:
#         break
# print(cnt)
# print(s)
# 1667229558.1148584
# 1667229592.6003969

for i in range(n - 1):
    for j in range(i+1, n):
        if arr[i] + arr[j] == x:
            cnt += 1
        if arr[i] + arr[j] > x:
            break


print(cnt)
# print(s)