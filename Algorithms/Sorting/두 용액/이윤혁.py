'''
정렬 알고리즘 + 투 포인터 알고리즘
(별다른 조건이 없을 시 sort로 정렬)
정렬 후 투 절대값 비교 & 투 포인터 활용
'''

import sys

N = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))
solutions.sort()
start = 0
end = len(solutions) - 1
best_sum = float('inf')
ans = (0, 0)

while start < end:
    current_sum = solutions[start] + solutions[end]
    if abs(current_sum) < abs(best_sum):
        best_sum = current_sum
        ans = (solutions[start], solutions[end])
        
    if current_sum > 0:
        end -= 1
    elif current_sum < 0:
        start += 1
    else:
        break

print(' '.join(map(str, ans)))