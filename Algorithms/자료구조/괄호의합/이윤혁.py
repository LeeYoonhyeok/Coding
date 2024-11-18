'''
여는 괄호가 나올 때
알맞는 괄호에 current_value에 값을 취해줌

닫는 괄호가 나올 때
stack이 비었거나 stack 마지막이 동일한 여는 괄호가 아니면 return 0
직전 괄호가 동일한 여는 괄호였으면 total_value에 current_value를 더해줌
stack pop하고 crruent는 나누기 -> 뒤에 단순 더하기 나올 수 있으므로 ex) [[][]] = 3*(3+3)
'''

import sys
input = sys.stdin.readline

def solution(st):
    stack = []
    total_value, current_value = 0, 1
    for i, char in enumerate(st):    
        if char == '(':
            stack.append(char)
            current_value *= 2
        elif char == '[':
            stack.append(char)
            current_value *= 3
        elif char == ')':
            if not stack or stack[-1] != '(':
                return 0
            if st[i-1] == '(':
                total_value += current_value
            stack.pop()
            current_value //= 2
        elif char == ']':
            if not stack or stack[-1] != '[':
                return 0
            if st[i-1] == '[':
                total_value += current_value
            stack.pop()
            current_value //= 3
            
    if stack:
        return 0
    
    return total_value

st = input().rstrip()
print(solution(st))