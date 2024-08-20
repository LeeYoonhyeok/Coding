'''
도전 실패 -> 답지 참고

새로운 조합 개수
n = 1 -> 1개
n = 2 -> 2개
n = 3 -> 5개
n = 4 -> 2개
n = 5 -> 2개
n = 6 -> 4개
n = 7 -> 2개
n = 8 -> 4개
n = 9 -> 4개
n = 4 이후로 새로운 조합 2 2 4 반복 출현
----
식 정리
dp[x] = dp[x-1] + 2*dp[x-2] + 5*dp[x-3] + 2*dp[x-4] + 2*dp[x-5] + 4*dp[x-6] + 2*dp[x-7] + 2*dp[x-8] + 4*dp[x-9]
dp[x+3] = dp[x+2] + 2*dp[x+1] + 5*dp[x] + 2*dp[x-1] + 2*dp[x-2] + 4*dp[x-3] + 2*dp[x-4] + 2*dp[x-5] + 4*dp[x-6]
-> dp[x+3] - dp[x] = dp[x+2] + 2*dp[x+1] + 5*dp[x] + dp[x-1] - dp[x-3]
-> dp[x+3] = dp[x+2] + 2*dp[x+1] + 6*dp[x] + dp[x-1] - dp[x-3]
-> dp[x] = dp[x-1] + 2*dp[x-2] + 6*dp[x-3] + dp[x-4] - dp[x-6]
'''

def solution(n):
    MOD = 1000000007
    dp = [0, 1, 3, 10, 23, 62, 170]
    
    if n < 7:
        return dp[n]
    
    for i in range(7, n + 1):
        x = (dp[-1] + 2*dp[-2] + 6*dp[-3]  + dp[-4] - dp[-6]) % MOD
        dp = dp[1:] + [x]
    return dp[-1]
