'''
stack의 마지막 height가 순회중인 i번째 height보다 작다면 버림 (pop)
위의 과정을 while문으로 돌려서 처리한 뒤, stack에 아직 남아있는 height가 있으면
i번째 height보다 stack의 마지막 height가 큰 것임
-> i번째는 stack의 마지막 height의 인덱스 + 1 번째로 쏘고 있음.
-> ans의 i번째에 삽입
'''

import sys
input = sys.stdin.readline

def solution(tops):
    stack = []
    for i in range(N):
        while stack and stack[-1][1] < tops[i]:
            stack.pop()
        
        if stack: 
            ans[i] = stack[-1][0] + 1
            
        stack.append((i, tops[i]))
    
    print(" ".join(map(str, ans)))
    
N = int(input())
tops = list(map(int, input().split()))
ans = [0] * N
solution(tops)