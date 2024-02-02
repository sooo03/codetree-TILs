# 오른쪽 열을 타일 하나로 채우는 경우 + 오른쪽 열을 타일 두개로 채우는 경우

n = int(input())
dp = [0] * 1001
dp[0], dp[1], dp[2] = 0, 1, 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])