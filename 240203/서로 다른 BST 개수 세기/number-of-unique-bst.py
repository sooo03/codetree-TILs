n = int(input())
dp = [0] * 20

for i in range(1, n+1):
    for j in range(0, j):
        dp[i] += dp[j] * dp[i-j-1]

print(dp[n])