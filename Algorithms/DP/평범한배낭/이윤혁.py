'''
dp문제. 배낭에 넣을 수 있는 최대의 물건의 가치 구하기
dp테이블에 최대 무게인 K부터 순회하고 있는 item의 weight까지 for문을 돌며 해당 구간의 dp마다 현재 or 물건을 넣었을 때를 비교하며 계산
'''
N, K = map(int, input().split())  # N: 물건의 개수, K: 배낭의 최대 무게
items = [list(map(int, input().split())) for _ in range(N)] # 각 물건의 무게와 가치

dp = [0] * (K + 1)
for weight, value in items:
    for w in range(K, weight-1, -1):
        dp[w] = max(dp[w], dp[w-weight] + value)
print(dp[K])












