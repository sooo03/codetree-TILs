n = int(input())
dp = [0 for _ in range(20)]

def count_bst(n):
    num_of_bst = 0
    for i in range(n):
        num_of_bst += dp[i] * dp[n-i-1]
    return num_of_bst

dp[0], dp[1] = 1, 1

for i in range(2, n+1):
    dp[i] = num_of_bst(i)

print(dp[n])