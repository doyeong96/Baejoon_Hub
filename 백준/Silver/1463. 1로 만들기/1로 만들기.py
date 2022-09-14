n = int(input())
# dp = [0] * (10**6 + 1)
dp = [0] * (n+1)
# dp[2] = 1
# dp[3] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    # 3의 배수
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
    # 2의 배수
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])

# print(dp)
print(dp[n])
