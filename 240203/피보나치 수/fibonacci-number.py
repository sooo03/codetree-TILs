n = int(input())
dp = [False for i in range(n+1)]
dp[1] = 1
dp[2] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])