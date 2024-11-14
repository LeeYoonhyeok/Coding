'''
오큰수 문제
- 오른쪽 숫자들중에 제일 왼쪽에 있는 큰 수 출력

이중 for문은 시간복잡도 O(N^2)으로 시간초과 발생
-> stack을 활용한 while문 활용하여 시간복잡도 O(N) 줄이기 가능
- while문은 push와 pop이 이루어질 때 한번만 실행되므로 배열 전체에 대해 총 N번 이하로 실행됨
'''

import sys
input = sys.stdin.readline

def solution():
    stack = []
    for i in range(N):
        while stack and numbers[stack[-1]] < numbers[i]:
            nge[stack.pop()] = numbers[i]
        stack.append(i)
N = int(input())
numbers = list(map(int, input().split()))
nge = [-1] * N
solution()
print(" ".join(map(str, nge)))