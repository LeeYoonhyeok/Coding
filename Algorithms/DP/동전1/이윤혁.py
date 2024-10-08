'''
동전을 순회하면서 dp를 점화식으로 채우기
'''
import sys
N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]

dp = [0] * (K+1)
dp[0] = 1

for coin in coins:
    for i in range(coin, K+1):
        dp[i] += dp[i - coin]
print(dp[-1])