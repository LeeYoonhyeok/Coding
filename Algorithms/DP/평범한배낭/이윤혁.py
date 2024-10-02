'''

'''
N, K = map(int, input().split())  # 물건의 개수, 배낭의 최대 무게
items = [list(map(int, input().split())) for _ in range(N)]  # 각 물건의 무게와 가치

# DP 배열 초기화 (1차원 배열 사용)
dp = [0] * (K + 1)

# DP 계산
for weight, value in items:
    for w in range(K, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

# 결과 출력
print(dp[K])