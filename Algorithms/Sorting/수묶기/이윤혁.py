'''
투포인트 알고리즘 사용 
2개의 수를 비교하며 계산해야하므로 left < right 말고, left <= right-1로 while 루트 작성
left == right 일 때는 1개의 수가 남은 것이므로 아래 조건문으로 확인 진행
배열을 정렬하여 투포인트 알고리즘을 사용하며 순회함
음수+0 과 양수를 나누어 따로 계산 진행함
'''
import sys
input = sys.stdin.readline

def find_max_sum(N, numbers):
    max_sum = 0
    left, right = 0, N-1
    
    while left <= right - 1: # 2개의 수를 묶어 계산해야하므로 left == right-1 은 2개의 수가 남은 것. left == right는 1개의 수가 남은 것. 그것은 아래에 따로 if 문으로 작성
        # 음수 or 0 존재        
        if numbers[left] <= 0: 
            if numbers[left+1] <= 0:
                max_sum += numbers[left] * numbers[left+1]
                left += 2
            else:
                max_sum += numbers[left]
                left += 1 
        # 양수만 존재           
        else:
            if numbers[right] + numbers[right-1] < numbers[right] * numbers[right-1]:
                max_sum += numbers[right] * numbers[right-1]
            else:
                max_sum += numbers[right] + numbers[right-1]
            right -= 2

    # 하나의 수가 남았을 때
    if left == right:
        max_sum += numbers[left]
                
    return max_sum

N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()
print(find_max_sum(N, numbers))