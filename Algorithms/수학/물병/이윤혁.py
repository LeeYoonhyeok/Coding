'''
같은 양의 물병 두 개를 합치는 방식으로 K개 만들기
-> 직접적으로 list나 deque로 구현하기엔 힘든 알고리즘 + 시간초과
-> 이진수로 변환하고 1의 개수를 파악하면 물통 N개로 만들 수 있는 물통의 수임
'''
import sys, time
from collections import deque
input = sys.stdin.readline

def solution(n, k):
    cnt_add = 0
    while bin(n).count('1') > k:
        n += 1
        cnt_add += 1
    return cnt_add
    
N, K = map(int, input().split())
print(solution(N, K))