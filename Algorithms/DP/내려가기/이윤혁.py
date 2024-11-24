'''
* 약간 이상한 문제 -> grid를 입력받고 시작하면 메모리 초과 발생
for문 내부에서 grid를 한 줄씩 입력받고 연산해야함 -> 메모리 사용 최소화
for문 내부에서 새로운 dp를 만들어 연산한 값을 저장함 그 후 원래 dp로 저장
'''
import sys
input = sys.stdin.readline

def calculate_sum(N):
    min_dp = [0] * 3
    max_dp = [0] * 3
    
    first_line = list(map(int, input().split()))
    for i in range(3):
        min_dp[i] = max_dp[i] = first_line[0][i]
    
    for i in range(1,N):
        line = list(map(int, input().split()))
        
        tmp_min_dp = [0] * 3
        tmp_max_dp = [0] * 3
        
        tmp_min_dp[0] = line[0] + min(min_dp[0], min_dp[1])
        tmp_min_dp[1] = line[1] + min(min_dp[0], min_dp[1], min_dp[2])
        tmp_min_dp[2] = line[2] + min(min_dp[1], min_dp[2])
        
        tmp_max_dp[0] = line[0] + max(max_dp[0], max_dp[1])
        tmp_max_dp[1] = line[1] + max(max_dp[0], max_dp[1], max_dp[2])
        tmp_max_dp[2] = line[2] + max(max_dp[1], max_dp[2])
        
        min_dp = tmp_min_dp
        max_dp = tmp_max_dp
                
    return max(max_dp), min(min_dp)

N = int(input())
max_ans, min_ans = calculate_sum(N)
print(max_ans, min_ans)