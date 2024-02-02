# 1층에서 n층까지 올라가는 경우의 수 = 1층에서 n-2층까지 경우의 수 + 1층에서 n-3층까지 경우의 수
#dp[n] = dp[n-2] + dp[n-3]

n = int(input())
dp = [0] * 1001
dp[0], dp[1], dp[2], dp[3] = 1, 0, 1, 1

for i in range(4, n+1):
    dp[i] = (dp[n-2] + dp[n-3]) % 10007
print(dp[n])