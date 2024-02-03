n = int(input())
dp = [0 for _ in range(20)]

def count_bst(n):
    bst_num = 0
    
    for i in range(n):
        bst_num += dp[i] * dp[n - i - 1]
        
    return bst_num


dp[0] = dp[1] = 1

for i in range(2, n + 1):
    dp[i] = count_bst(i)
    
print(dp[n])