import sys
N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
dp = [float('inf')] * (K+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, K+1):
        dp[i] = min(dp[i], dp[i-coin]+1)
        
if dp[K] == float('inf'):
    print(-1)
else:
    print(dp[K])