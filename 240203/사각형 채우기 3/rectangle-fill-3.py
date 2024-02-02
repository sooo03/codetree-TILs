MOD = 1000000007

n = int(input())
A = [0]*1001

#마지막 1개가 한칸만 채워진 경우
B = [0]*1001

A[1], A[2]= 2, 7
B[1], B[2]= 1, 3

for i in range(3, n+1):
    A[i] = (A[i-1]*2 + A[i-2] + B[i-1] * 2 )  % MOD
    B[i] = (A[i-1] + B[i-1]) % MOD

print(A[n])