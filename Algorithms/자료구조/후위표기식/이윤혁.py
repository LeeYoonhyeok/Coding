import sys
input = sys.stdin.readline

def solution(st):
    precedence = {'+':1, '-':1, '*':2, '/':2, '(':0} # 우선순위 설정
    stack = []
    ans = ''
    
    for char in st:
        if char.isalpha():
            ans += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        else:
            while stack and precedence[stack[-1]] >= precedence[char]:
                ans += stack.pop()
            stack.append(char)
            
    while stack:
        ans += stack.pop()
                
    return ans

st = input().rstrip()
print(solution(st))
        