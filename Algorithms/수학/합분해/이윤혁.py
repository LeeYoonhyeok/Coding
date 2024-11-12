'''
K개의 숫자들의 합으로 숫자 N을 만드는 경우의 수
dp문제
'''

import sys

MOD = 1000000000
N, K = map(int, sys.stdin.readline().split())
dp = [[0] * (N+1) for _ in range(K+1)]

for i in range(N+1): # 숫자 하나로 i 만드는 경우의 수 = 1
    dp[1][i] = 1
    
for i in range(K+1): # 0을 만드는 경우의 수 = 1
    dp[i][0] = 1
    
for i in range(2, K+1):
    for j in range(1, N+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
        
print(dp[-1][-1])
